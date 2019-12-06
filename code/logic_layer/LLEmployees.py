class LLEmployees:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_employee_list = []

    def validate_employee(self):
        pass

    def get_all_employees(self):
        ''' pulls and returns a list of employee instances '''
        return self.__dl_api.populate_all_employees()

    def push_all_employees(self, all_employees):
        self.__dl_api.overwrite_all_employees(all_employees)

    def list_all_employees_by_name(self):
        all_employee_list = self.get_all_employees()

        return sorted(all_employee_list, key=lambda employee: employee.get_name())

    def get_name_dict(self):
        ''' gets a list of employee instances and returns a dict where key is name and value is ssn '''
        employee_list = self.get_all_employees()
        name_dict = {}
        for employee in employee_list:
            name_dict[employee.get_name()] = employee.get_ssn()
        return name_dict

    def get_employees_by_name(self, search_string):
        ''' pulls a list of employee instances and returns a instance of employee by employee_ID '''

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
        employee_list = self.__dl_api.populate_all_employees()
        for employee in employee_list:
            if employee.get_title() == title:
                filter_list.append(employee)
        return filter_list

    def filter_pilots_by_airplane_type(self, airplane_type):
        pass

    def sort_pilots_by_airplane_type(self):
        pass

    def edit_employee(self, employee, input_tpl):
        ''' gets an instance and a tuple that holds a input flag and input string,
            calls a set function depending on flag and returns a boolean '''
        set_employee_info_dict = {0:employee.set_home_address, 1:employee.set_home_number, 2:employee.set_mobile_number, 
                                    3:employee.set_email, 4:employee.set_title, 5:employee.set_rank}
        success_check = set_employee_info_dict[input_tpl[0]](input_tpl[1])
        if success_check:
            self.__dl_api.overwrite_all_employees(self.__all_employee_list)
        return success_check

    def create_work_scedule(self):
        pass
