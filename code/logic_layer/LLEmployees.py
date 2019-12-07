from datetime import datetime

class LLEmployees:
    DOMAIN = "@nanair.is"
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_employee_list = []

        

    def validate_employee(self, employee):
        ''' Gets employee instance and returns a boolean '''
        return self.__modelAPI.validate_model(employee)

    def email_generator(self,name):
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
        if self.validate_employee(employee):
            self.__dl_api.append_employee(employee)
            return True
            
        return False

    def get_all_employees(self):
        ''' Pulls and returns a list of employee instances '''
        return self.__dl_api.pull_all_employees()

    def push_all_employees(self, all_employee_list):
        ''' Takes a list of employee instances and sends it to the DL '''
        self.__dl_api.overwrite_all_employees(all_employee_list)

    def list_all_employees_by_name(self):
        all_employee_list = self.get_all_employees()

        return sorted(all_employee_list, key=lambda employee: employee.get_name())

    def get_name_dict(self):
        ''' Gets a list of employee instances and returns a dict where key is name and value is ssn '''
        employee_list = self.get_all_employees()
        name_dict = {}
        for employee in employee_list:
            name_dict[employee.get_name()] = employee.get_ssn()
        return name_dict

    def get_employees_by_name(self, search_string):
        ''' Pulls a list of employee instances and returns a list of instances based on search_string '''

        name_dict = self.get_name_dict()
        found_ssn_list = []
        found_employee_list = []

        for name, ssn in name_dict.items():
            if search_string in name:
                found_ssn_list.append(ssn)

        self.__all_employee_list = self.get_all_employees()

        for employee in self.__all_employee_list:
            if employee.get_ssn() in found_ssn_list:
                found_employee_list.append(employee)
        return found_employee_list

    def get_one_employee(self, ssn):
        self.__all_employee_list = self.get_all_employees()

        for employee in self.__all_employee_list:
            if employee.get_ssn() == ssn:
                return employee

    def list_all_employees_by_date(self):
        pass

    def filter_all_employees_by_availability(self):
        pass

    def filter_all_employees_by_title(self, title):
        ''' Takes list of all employees and returns list of employees filtered by title from input '''

        filter_list = []
        employee_list = self.__dl_api.pull_all_employees()
        for employee in employee_list:
            if employee.get_title() == title:
                filter_list.append(employee)
        return filter_list

    def filter_pilots_by_airplane_type(self, airplane_type):
        pilot_list = self.sort_pilots_by_airplane_type()
        
        filter_list = []
        for pilot in pilot_list:
            if pilot.get_licence() == airplane_type:
                filter_list.append(pilot)
        return filter_list

    def sort_pilots_by_airplane_type(self):
        ''' Gets a list of pilots and returns it sorted '''
        title = "Pilot"
        pilot_list = self.filter_all_employees_by_title(title)
        return sorted(pilot_list, key=lambda employee: employee.get_licence())

    def edit_employee(self, employee, input_tpl):
        ''' Gets an instance and a tuple that holds a input flag and input string,
            calls a set function depending on flag and returns a boolean '''

        set_employee_info_dict = {0:employee.set_home_address, 
                                  1:employee.set_home_number,
                                  2:employee.set_mobile_number, 
                                  3:employee.set_title, 
                                  4:employee.set_rank}
        success_check = set_employee_info_dict[input_tpl[0]](input_tpl[1])
        if success_check:
            self.__dl_api.overwrite_all_employees(self.__all_employee_list)
        return success_check

    def get_work_schedule_list(self, employee):
        '''Gets list of all voyages and instance of employee, returns voyages employee is working in the future'''
        all_voyage_list = self.__dl_api.pull_all_voyages()
        upcoming_voyages = []
        current_date = datetime.now().replace(microsecond=0).isoformat()
        for voyage in all_voyage_list:
            if (employee.get_ssn() == voyage.get_voyage_employee_ssn(employee.get_rank())
            and (voyage.get_departing_flight_departure_date() >= current_date)):
                upcoming_voyages.append(voyage)
        return upcoming_voyages 
    
