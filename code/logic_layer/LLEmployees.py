from datetime import datetime
from datetime import timedelta
class LLEmployees:
    DOMAIN = "@nanair.is"
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_employee_list = []

        self.__ll_voyages = None
        self.__ll_airplanes = None

    def set_ll_voyages(self, ll_voyage):
        self.__ll_voyages = ll_voyage

    def set_ll_airplanes(self, ll_airplanes):
        self.__ll_airplanes = ll_airplanes

    # All list functions

    def get_all_employee_list(self, changed = False):
        ''' Pulls and returns a list of employee instances '''
        if changed:
            self.__all_employee_list = self.__dl_api.pull_all_employees()
        if not self.__all_employee_list:
            self.__all_employee_list = self.__dl_api.pull_all_employees()
        self.get_working_or_not()
        return self.__all_employee_list

    def sort_all_employees_by_name(self):
        return sorted(self.get_all_employee_list(), key=lambda employee: employee.get_name())

    def filter_employees_by_name(self, search_string):
        ''' Pulls a list of employee instances and returns a list of instances based on search_string '''

        name_dict = self.get_name_dict()
        found_ssn_list = []
        found_employee_list = []

        for name, ssn in name_dict.items():
            if search_string in name:
                found_ssn_list.append(ssn)

        for employee in self.__all_employee_list:
            if employee.get_ssn() in found_ssn_list:
                found_employee_list.append(employee)

        return sorted(found_employee_list, key=lambda employee: employee.get_name())

    def filter_all_employees_by_title(self, title):
        '''Gets a list of all employees and returns a list of employees filtered by title from input'''

        filter_list = []
        for employee in self.get_all_employee_list():
            if employee.get_title() == title:
                filter_list.append(employee)
        return sorted(filter_list, key=lambda employee: employee.get_name())

    def sort_pilots_by_airplane_type(self):
        '''Gets a list of pilots and returns it sorted'''
        title = "Pilot"
        pilot_list = self.filter_all_employees_by_title(title)
        return sorted(pilot_list, key=lambda employee: employee.get_licence())

    def filter_pilots_by_airplane_type(self, airplane_type):
        '''Gets a list of all pilots and returns a list of pilots filtered by airplane type'''
        pilot_list = self.sort_pilots_by_airplane_type()
        
        filter_list = []
        for pilot in pilot_list:
            if pilot.get_licence() == airplane_type:
                filter_list.append(pilot)
        
        return sorted(filter_list, key=lambda employee: employee.get_name())

    def get_work_schedule_list(self, employee):
        '''Gets list of all voyages and instance of employee, returns voyages employee is working in the future'''
        all_voyage_list = self.__ll_voyages.get_all_voyage_list()
        upcoming_voyages = []
        current_date = datetime.now().replace(microsecond=0)

        for voyage in all_voyage_list:
            voyage_ssn = voyage.get_voyage_employee_ssn(employee.get_rank())
            start_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())

            if type(voyage_ssn).__name__ == "list":
                if employee.get_ssn() in voyage_ssn and start_date >= current_date:
                    upcoming_voyages.append(voyage)

            elif employee.get_ssn() == voyage_ssn and start_date >= current_date:
                upcoming_voyages.append(voyage)

        return sorted(upcoming_voyages, key=lambda voyage: voyage.get_departing_flight_departure_date())

    def get_all_licences(self):
        return self.__ll_airplanes.get_airplane_type_list()

    # All change functions

    def create_employee(self, employee):
        employee.set_email(self.email_generator(employee.get_name()))
        if self.__modelAPI.validate_model(employee):
            if self.__dl_api.append_employee(employee):
                self.get_all_employee_list(True)
                return True
            
        return False

    def overwrite_all_employees(self):
        ''' Takes a list of employee instances and sends it to the DL '''
        if self.__dl_api.overwrite_all_employees(self.__all_employee_list):
            self.get_all_employee_list(True)
            return True


    def turn_iso_format_friendly(self, date, time):
        '''Honestly, I don't know what to tell you'''
        day, month, year = date.split("-")
        return "{}-{}-{}T{}".format(year,month,day,time)


    def filter_working(self, date, hours, flag):
        self.get_all_employee_list()
        self.get_working_or_not(self.turn_iso_format_friendly(date,hours))
        return_list = []
        if flag.lower() == "working":
            for employee in self.__all_employee_list:
                if employee.get_availability() == "Not available":
                    return_list.append(employee)
        else:
            for employee in self.__all_employee_list:
                if employee.get_availability() == "Available":
                    return_list.append(employee)
        return return_list

    def check_employee_status(self, datetime_input):
        pass



    def get_working_or_not(self, date = datetime.today().replace(microsecond=0).isoformat()):
        all_voyage_list = self.__ll_voyages.get_all_voyage_list()
        
        working = []
        not_working = []
        current_time = self.get_iso_format_date_time(date)
        start_range= current_time.replace(hour=0, minute=0,second=0,microsecond=0)
        end_range = start_range + timedelta(hours = 23, minutes=59, seconds=59)

        for employee in self.__all_employee_list:
            employee_ssn = employee.get_ssn()
            for voyage in all_voyage_list:
                departing_flight_departure_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
                departing_flight_arrival_date = self.get_iso_format_date_time(voyage.get_departing_flight_arrival_date())
                return_flight_departure_date = self.get_iso_format_date_time(voyage.get_return_flight_departure_date())
                return_flight_arrival_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

                fa_ssns = voyage.get_fa_ssns()
                captain_ssn = voyage.get_captain_ssn()
                co_pilot_ssn = voyage.get_copilot_ssn()
                fsm_ssn = voyage.get_fsm_ssn()
                if employee_ssn in fa_ssns or employee_ssn == captain_ssn or employee_ssn == co_pilot_ssn or employee_ssn == fsm_ssn:
                    if start_range <= departing_flight_departure_date <= end_range or start_range <= return_flight_arrival_date <= end_range:
                        if employee not in working:
                            working.append(employee)
                            employee.set_availability("Not available")
                            
                    if current_time <= departing_flight_departure_date:
                        employee.set_current_destination("Stationed in {}".format(voyage.get_departing_flight_departing_from()))
                    elif departing_flight_departure_date <= current_time <= departing_flight_arrival_date:
                        employee.set_current_destination("Flying to {}".format(voyage.get_return_flight_departing_from()))
                    elif departing_flight_arrival_date <= current_time <= return_flight_departure_date:
                        employee.set_current_destination("Stationed in {}".format(voyage.get_return_flight_departing_from()))
                    elif return_flight_departure_date <= current_time <= return_flight_arrival_date:
                        employee.set_current_destination("Flying to {}".format(voyage.get_departing_flight_departing_from()))
                    else:
                        voyage.set_status("Voyage completed")

            if employee not in not_working  and employee not in working:
                not_working.append(employee)
                employee.set_availability("Available")



    # All special functions

    def get_one_employee(self, ssn):
        '''Shows information about one employee'''
        for employee in self.get_all_employee_list():
            if employee.get_ssn() == ssn:
                return employee

    def get_name_dict(self):
        ''' Gets a list of employee instances and returns a dict where key is name and value is ssn '''
        self.get_all_employee_list()
        name_dict = {}
        for employee in self.__all_employee_list:
            name_dict[employee.get_name()] = employee.get_ssn()
        return name_dict

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

    def email_generator(self,name):
        '''Makes a new e-mail address for a new employee'''
        name = (name.replace(" ",".")).lower()
        all_employees = self.__dl_api.pull_all_employees()
        all_existing_emails = [x.get_email() for x in all_employees]
        number = 0
        temp_name  = name
        while temp_name + self.DOMAIN in all_existing_emails:
            number += 1
            temp_name = name + str(number)
            
        return name + self.DOMAIN