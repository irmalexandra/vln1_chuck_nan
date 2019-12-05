class LLEmployees:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_employee(self):
        pass

    def get_all_employees(self):
        ''' pulls and returns a list of employee instances '''
        return self.__dl_api.populate_all_employees()

    def list_all_employees_by_name(self):
        all_employee_list = self.get_all_employees()

        return sorted(all_employee_list, key=lambda employee: employee.get_name())

    def get_name_dict(self):
        employee_list = self.get_all_employees()
        name_dict = {}
        for employee in employee_list:
            name_dict[employee.get_name()] = employee.get_ssn()
        return name_dict

    def get_employee_by_name(self, name):
        ''' pulls a list of employee instances and returns a instance of employee by employee_ID '''
        name_dict = self.get_name_dict()
        employee_ssn = name_dict[name]

        employee_list = self.get_all_employees()

        for employee in employee_list:
            if employee.get_ssn() == employee_ssn:
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

    def create_work_scedule(self):
        pass
