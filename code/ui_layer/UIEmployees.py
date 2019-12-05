class UIEmployees():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    def display_employee_sub_menu(self):
        while True:

            nav_dict = {1: self.create_employee, 2: self.display_all_employees, 3: self.display_employee_search_menu,
                        9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
            employee_menu = "1. Create 2. All 3. Search by"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(employee_menu, " "*(self.UI_DIVIDER_INT -
                                                        len(employee_menu) -
                                                        len(self.RETURN_MENU_STR)
                                                        - self.DEVIATION_INT), self.RETURN_MENU_STR))

            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice = nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def display_employee_search_menu(self):
        ''' Print the search menu of employee sub menu '''
        # needs input
        while True:

            nav_dict = {1: self.get_employee_by_name, 2: self.display_all_employees_by_title, 3: self.display_all_employees_by_date,
                        4: self.display_all_employees_by_title, 9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
            search_menu = "1. Name 2. Title 3. Date 4. Airplane"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(search_menu, " "*(self.UI_DIVIDER_INT -
                                                      len(search_menu) - len(self.RETURN_MENU_STR) -
                                                      self.DEVIATION_INT), self.RETURN_MENU_STR))

            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice = nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def get_employee_by_name(self, name):
        ''' Search for employee instance and print out it's information '''
        self.display_employee(self.__ll_api.get_employee_by_name(name))

    def display_employee(self, employee):
        print(employee)

    def display_edit_employee(self):
        pass

    def display_all_employees(self):
        ''' Print the given dictionary of employees '''
        nav_dict = {9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        while True:
            print("-" * self.UI_DIVIDER_INT)
            print("|{:<10}{:20}{:15}{:20}{:20}{:10}|".format(
                "Index: ", "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
            employee_list = self.__ll_api.get_employee_list_by_name()
            for index, employee in enumerate(employee_list):
                print("|{:02d}{:<8}{:20}{:15}{:20}{:20}{:10}|".format(index+1, "",
                                                                      employee.get_name(),
                                                                      employee.get_ssn(),
                                                                      employee.get_address(),
                                                                      employee.get_mobile_num(),
                                                                      employee.get_title()))
            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice = nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def display_all_employees_by_date(self):
        '''Displays all employees availability on a specific day'''
        # needs input
        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Mobile Number:", "Title:", "Availability:"))
        employee_list = self.__ll_api.get_all_employee_list()
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title(),
                                                       "Missing availability"))
        print("-" * self.UI_DIVIDER_INT)

    def display_all_employees_by_title(self, title):
        ''' Print a filtered list of all employees by title '''

        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
        employee_list = self.__ll_api.get_employee_dict_by_title(title)
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_address(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title()))
        print("-" * self.UI_DIVIDER_INT)

    def display_pilots_by_airplane_type_sorted(self):
        ''' print a sorted list of pilots '''

        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
        employee_list = self.__ll_api.get_employee_list_by_title("Pilot")
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_address(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title()))
        print("-" * self.UI_DIVIDER_INT)

    def display_pilots_by_airplane_type_filtered(self, airplane_type):
        pass

    def create_employee(self):
        ''' Create an employee, if employee is a pilot licence and rank is input '''
        title = input("Title: ")
        new_emp = self.__modelAPI.get_model(title)
        if title == "Pilot":
            licence = input("Licence: ")
            new_emp.set_licence(licence)
            rank = input("Rank: ")
            new_emp.set_rank(rank)
        name = input("Name: ")
        new_emp.set_name(name)
        ssn = input("SSN: ")
        new_emp.set_ssn(ssn)
        home_number = input("Home number: ")
        new_emp.set_home_num(home_number)
        mobile_number = input("Mobile number: ")
        new_emp.set_mobile_num(mobile_number)
        email = input("E-mail: ")
        new_emp.set_email(email)

    def edit_employee(self):
        pass

    def change_airplane_type(self):
        pass
