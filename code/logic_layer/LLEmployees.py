from datetime import datetime

class LLEmployees:
    DOMAIN = "@nanair.is"
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_employee_list = []

    def validate_new_employee(self, employee):
        '''Gets employee instance and returns a boolean'''
        return self.__modelAPI.validate_create_model(employee)

    def validate_edited_employee(self, employee):
        '''Gets employee instance and returns a boolean'''
        return self.__modelAPI.validate_edit_model(employee)

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


    def create_employee(self, employee):
        employee.set_email(self.email_generator(employee.get_name()))
        if self.validate_new_employee(employee):
            self.__dl_api.append_employee(employee)
            return True
            
        return False

    def get_all_employee_list(self):
        ''' Pulls and returns a list of employee instances '''
        self.__all_employee_list = self.__dl_api.pull_all_employees()
        return self.__all_employee_list

    def overwrite_all_employees(self):
        ''' Takes a list of employee instances and sends it to the DL '''
        return self.__dl_api.overwrite_all_employees(self.__all_employee_list)

    def sort_all_employees_by_name(self):
        return sorted(self.get_all_employee_list(), key=lambda employee: employee.get_name())

    def get_name_dict(self):
        ''' Gets a list of employee instances and returns a dict where key is name and value is ssn '''
        employee_list = self.get_all_employee_list()
        name_dict = {}
        for employee in employee_list:
            name_dict[employee.get_name()] = employee.get_ssn()
        return name_dict

    def filter_employees_by_name(self, search_string):
        ''' Pulls a list of employee instances and returns a list of instances based on search_string '''

        name_dict = self.get_name_dict()
        found_ssn_list = []
        found_employee_list = []

        for name, ssn in name_dict.items():
            if search_string in name:
                found_ssn_list.append(ssn)

        for employee in self.get_all_employee_list():
            if employee.get_ssn() in found_ssn_list:
                found_employee_list.append(employee)
        return found_employee_list

    def get_one_employee(self, ssn):
        '''Shows information about one employee'''
        for employee in self.get_all_employee_list():
            if employee.get_ssn() == ssn:
                return employee

    def list_all_employees_by_date(self):
        pass

    def filter_all_employees_by_availability(self):        
        '''Gets a list of all employees and returns a list of employees filtered by availability'''
        pass

    def filter_all_employees_by_title(self, title):
        '''Gets a list of all employees and returns a list of employees filtered by title from input'''

        filter_list = []
        for employee in self.get_all_employee_list():
            if employee.get_title() == title:
                filter_list.append(employee)
        return filter_list

    def filter_pilots_by_airplane_type(self, airplane_type):
        '''Gets a list of all pilots and returns a list of pilots filtered by airplane type'''
        pilot_list = self.sort_pilots_by_airplane_type()
        
        filter_list = []
        for pilot in pilot_list:
            if pilot.get_licence() == airplane_type:
                filter_list.append(pilot)
        return filter_list

    def sort_pilots_by_airplane_type(self):
        '''Gets a list of pilots and returns it sorted'''
        title = "Pilot"
        pilot_list = self.filter_all_employees_by_title(title)
        return sorted(pilot_list, key=lambda employee: employee.get_licence())

    def get_work_schedule_list(self, employee):
        '''Gets list of all voyages and instance of employee, returns voyages employee is working in the future'''
        all_voyage_list = self.__dl_api.pull_all_voyages()
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

        return upcoming_voyages 

    def get_working_or_not(self, date, flag):
        all_voyage_list = self.__dl_api.pull_all_voyages()
        all_employee_list = self.get_all_employee_list()
        working = []
        not_working = []
        date_instance = self.get_iso_format_date_time(date)
        for voyage in all_voyage_list:
            if self.get_iso_format_date_time(voyage.get_departing_flight_departure_date()) <= date_instance <= self.get_iso_format_date_time(voyage.get_return_flight_arrival_date()):
                fa_ssns = voyage.get_fa_ssns()
                captain_ssn = voyage.get_captain_ssn()
                co_pilot_ssn = voyage.get_copilot_ssn()
                fsm_ssn = voyage.get_fsm_ssn()

                for employee in all_employee_list:
                    employee_ssn = employee.get_ssn()
                    if employee_ssn in fa_ssns or employee_ssn == captain_ssn or employee_ssn == co_pilot_ssn or employee_ssn == fsm_ssn:
                        working.append(employee)
                    else:
                        not_working.append(employee)

        if flag.lower() == "working":
            return working
        else:
            return not_working


    
    def get_iso_format_date_time(self, date=''):

        if date.find("T") == -1:
            date = datetime.strptime(date,'%d-%m-%Y')
        else:
            date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')

        return date

    def get_all_licences(self):
        return self.__dl_api.pull_all_airplane_types()
