from datetime import datetime
from datetime import timedelta
class LLVoyages:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_voyage_list = []

    # All list functions

    def get_all_voyage_list(self, changed = False):

        if changed:
            self.__all_voyage_list = self.__dl_api.pull_all_voyages()
        elif not self.__all_voyage_list:
            self.__all_voyage_list = self.__dl_api.pull_all_voyages()

        self.check_status()
        self.check_staffed()
        return sorted(self.__all_voyage_list, key=lambda voyage: voyage.get_departing_flight_departure_date())

    def filter_all_empty_voyages(self):
        '''Takes a list of all voyage instances and returns a list of filtered voyage instances'''
        self.get_all_voyage_list() 
        empty_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_airplane_insignia() == ".":
                empty_voyage_list.append(voyage)

        return sorted(empty_voyage_list, key=lambda voyage: voyage.get_departing_flight_departure_date())

    def filter_all_voyages_by_period(self, start_date, end_date):
        '''Takes a list of all voyage instances and returns a list of voyages filteres by period'''
        self.get_all_voyage_list()

        start = self.get_iso_format_date_time(start_date)
        end = self.get_iso_format_date_time(end_date)
        
        period_voyage_list = []

        for voyage in self.__all_voyage_list:
            if start <= self.get_iso_format_date_time(voyage.get_return_flight_arrival_date()) and self.get_iso_format_date_time(voyage.get_departing_flight_departure_date()) <= end:
                period_voyage_list.append(voyage)
        return period_voyage_list
        
    def filter_all_voyages_by_airport(self, airport):

        self.get_all_voyage_list()
        airport_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_return_flight_departing_from() == airport:
                airport_voyage_list.append(voyage)

        return airport_voyage_list

    def filter_available_employees(self, rank, voyage):

        start_date = voyage.get_departing_flight_departure_date()
        end_date = voyage.get_return_flight_arrival_date()
        voyages_in_date_range_list = self.filter_all_voyages_by_period(start_date, end_date)

        all_employee_list = self.__dl_api.pull_all_employees() #note meiga allir LL layers tala á milli sýn? til þess að geta nýtt update status í ll employees

        filter_rank_list = [(employee) for employee in all_employee_list if employee.get_rank() == rank]

        available_employee_list = []

        for other_voyage in voyages_in_date_range_list:   
            voyage_ssn = other_voyage.get_voyage_employee_ssn(rank)
            for employee in filter_rank_list:
                if employee not in available_employee_list:
                    employee_ssn = employee.get_ssn()
                    if type(voyage_ssn).__name__ == "list":
                        if employee_ssn not in voyage_ssn:
                            available_employee_list.append(employee)
                            
                    else:
                        if employee_ssn != voyage_ssn:
                            available_employee_list.append(employee)

        final_employee_list = available_employee_list    
        
        if rank == "Captain" or rank == "Copilot":
            final_employee_list = []
            for airplane in self.__dl_api.pull_all_airplanes():
                if airplane.get_insignia() == voyage.get_airplane_insignia():
                    selected_airplane = airplane
                    break

            airplane_type = "NA" + selected_airplane.get_make() + selected_airplane.get_model()

            for employee in available_employee_list: 
                if employee.get_licence() == airplane_type:
                    final_employee_list.append(employee)

        return sorted(final_employee_list, key=lambda employee: employee.get_name())

    # All change functions

    def create_voyage(self, airport, start_date = "00-00-0000", start_time = "00:00:00"):

        self.get_all_voyage_list()
        if type(start_date).__name__ != "datetime":
            try:
                fixed_date = datetime.strptime(start_date, '%d-%m-%Y')
                fixed_time = datetime.strptime(start_time, '%H:%M:%S').time()
            except ValueError:
                return False
            fixed_date_time = datetime.combine(fixed_date, fixed_time)
        else:
            fixed_date_time = start_date
        
        new_voyage = self.__modelAPI.get_model("Voyage")

        new_voyage.set_return_flight_departing_from(airport)
        new_voyage.set_departing_flight_departure_date(fixed_date_time.isoformat())
        new_voyage.set_airplane_insignia(".")
        new_voyage.set_captain_ssn(".")
        new_voyage.set_copilot_ssn(".")
        new_voyage.set_fsm_ssn(".")
        new_voyage.set_fa_ssns([".", "."])

        dep_flight_num, ret_flight_num = self.generate_flight_numbers(start_date, airport) 
        new_voyage.set_flight_numbers(dep_flight_num, ret_flight_num)

        departing_flight_arrival_date_str, return_flight_departure_date_str, return_flight_arrival_date_str \
            = self.calculate_flight_times(fixed_date_time, airport)
        
        new_voyage.set_flight_times(departing_flight_arrival_date_str, \
            return_flight_departure_date_str, return_flight_arrival_date_str)

        start_date = fixed_date_time.isoformat()
        end_date = new_voyage.get_return_flight_arrival_date()

        for voyage in self.__all_voyage_list:
            other_start_date = voyage.get_departing_flight_departure_date()
            other_end_date = voyage.get_return_flight_arrival_date()
            
            if other_start_date == start_date or other_start_date == end_date or\
                other_end_date == start_date or other_end_date == end_date:
                return False

        if self.__modelAPI.validate_model(new_voyage):
            if self.__dl_api.append_voyage(new_voyage):
                self.get_all_voyage_list(True)
                return True

        return False

    def overwrite_all_voyages(self):
        if self.__dl_api.overwrite_all_voyages(self.__all_voyage_list):
            self.get_all_voyage_list(True)
            return True

    def duplicate_voyage(self, voyage, start_date = "00-00-0000", start_time = "00:00:00"):
        '''Copies a voyage to another date'''

        destination = voyage.get_destination()
        return self.create_voyage(destination, start_date, start_time)

    def repeat_voyage(self, voyage, repeat_interval, end_date = "00-00-0000"):
        success = False
        try:
            date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
            end_date = self.get_iso_format_date_time(end_date)
            repeat_interval = int(repeat_interval)
        except ValueError:
            return False
        while date <= end_date:
            date += timedelta(days=repeat_interval)
            success = self.duplicate_voyage(voyage, date)
        return success
            
    def add_employee_to_voyage(self, voyage, employee):
        rank_dict = {'Captain':voyage.set_captain_ssn, 
                     'Copilot':voyage.set_copilot_ssn, 
                     'Flight Service Manager':voyage.set_fsm_ssn, 
                     'Flight Attendant':voyage.set_fa_ssns}

        employee_ssn_str = employee.get_ssn()
        employee_rank_str = employee.get_rank()
        check = rank_dict[employee_rank_str](employee_ssn_str)
        if check:
            return self.overwrite_all_voyages()
        return check
    
    def add_airplane_to_voyage(self, voyage, airplane):
        if voyage.set_airplane_insignia(airplane.get_insignia()):
            return self.overwrite_all_voyages()
            
        
    def check_status(self):
        current_date = datetime.today()
        for voyage in self.__all_voyage_list:
            departing_flight_departure_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
            departing_flight_arrival_date = self.get_iso_format_date_time(voyage.get_departing_flight_arrival_date())
            return_flight_departure_date = self.get_iso_format_date_time(voyage.get_return_flight_departure_date())
            return_flight_arrival_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

            if current_date <= departing_flight_departure_date:
                voyage.set_status("Not started")
            elif departing_flight_departure_date <= current_date <= departing_flight_arrival_date:
                voyage.set_status("Flying to {}".format(voyage.get_return_flight_departing_from()))
            elif departing_flight_arrival_date <= current_date <= return_flight_departure_date:
                voyage.set_status("Currently in {}".format(voyage.get_return_flight_departing_from()))
            elif return_flight_departure_date <= current_date <= return_flight_arrival_date:
                voyage.set_status("Flying to {}".format(voyage.get_departing_flight_departing_from()))
            else:
                voyage.set_status("Voyage completed")
    
    def check_staffed(self):
        for voyage in self.__all_voyage_list:
            if voyage.get_airplane_insignia() != "." and voyage.get_captain_ssn() != "." and voyage.get_copilot_ssn() != "." and voyage.get_fsm_ssn() != "." and voyage.get_fa_ssns() != ".:.":
                voyage.set_staffed("Staffed")
            else:
                voyage.set_staffed("Not staffed")

    # All special functions

    def calculate_flight_times(self, date, airport):
        self.__all_voyage_list = self.get_all_voyage_list()
        destinations_list = self.__dl_api.pull_all_destinations()
        destinations_dict = dict()
        
        for destination in destinations_list:
            destinations_dict[destination.get_airport()] = int(destination.get_flight_time())
        
        flight_time = destinations_dict[airport]
        departing_flight_arrival_date = date + timedelta(hours =flight_time)
        return_flight_departure_date = departing_flight_arrival_date + timedelta(hours = 1)
        return_flight_arrival_date = return_flight_departure_date + timedelta(hours = flight_time)
        return departing_flight_arrival_date.isoformat(), return_flight_departure_date.isoformat(), return_flight_arrival_date.isoformat()

    def generate_flight_numbers(self, date, airport):
        NEW_FLIGHT_NUM_LEN = 7
        LAST_POSSIBLE_FLIGHT = 999
        start_date = self.get_iso_format_date_time(date)
        end_date = start_date + timedelta(hours=23, minutes=59,seconds=59)
        all_destinations_list = self.__dl_api.pull_all_destinations()

        for destination in all_destinations_list:
            if airport == destination.get_airport():
                destination_id = destination.get_destination_id()

        self.__all_voyage_list = self.get_all_voyage_list()
        existing_numbers = []

        for voyage in self.__all_voyage_list:
            voyage_airport = voyage.get_return_flight_departing_from()
            departing_flight_departure_date = self.get_iso_format_date_time(voyage.get_return_flight_departure_date())
            if start_date <= departing_flight_departure_date <= end_date and voyage_airport == airport:
                flight_number = voyage.get_return_flight_num()
                if len(flight_number) == NEW_FLIGHT_NUM_LEN:
                    existing_numbers.append(int(flight_number.replace("NA" + destination_id,"")))

        if LAST_POSSIBLE_FLIGHT in existing_numbers:
            return False
        else:
            last_number = max(existing_numbers)
            next_departing_number_str  = str(last_number + 1)
            next_return_number_str = str(last_number + 2)
            while len(next_departing_number_str) < 4:
                next_departing_number_str = "0" + next_departing_number_str
            while len(next_return_number_str) < 4:
                next_return_number_str = "0" + next_return_number_str
            
            departing_flight_num = "NA" + destination_id + str(next_departing_number_str)
            return_flight_num = "NA" + destination_id + str(next_return_number_str)
            return departing_flight_num, return_flight_num


    def get_iso_format_date_time(self, date = "00-00-0000", time = "00:00:00"):
        if type(date).__name__ != 'datetime':

            if date.find("T") == -1:
                new_date = datetime.strptime(date,'%d-%m-%Y')
                new_time = datetime.strptime(time, '%H:%M:%S').time()
                new_date = datetime.combine(new_date, new_time)
            else:
                new_date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
            return new_date
        return date

    def update_voyage_pointer(self, voyage):
        for updated_voyage in self.__all_voyage_list:
            if voyage.get_departing_flight_departure_date() == updated_voyage.get_departing_flight_departure_date():
                return updated_voyage