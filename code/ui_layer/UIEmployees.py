class UIEmployees():
    UI_DIVIDER_INT = 124
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2
    WALL = "|"

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    def display_employee_sub_menu(self):
        nav_dict = {1: self.create_employee, 2: self.display_all_employees, 3: self.display_employee_search_menu,
                    9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Create 2. Display all 3. Search by"
        return_bool = self.__ui_base_functions.display_menu(
            employee_menu, nav_dict)
        if return_bool == 0:
            return 0
        if return_bool == 9:
            return

    def display_employee_search_menu(self):
        ''' Print the search menu of employee sub menu '''
        nav_dict = {1: self.get_employee_by_name, 2: self.display_all_employees_by_title, 3: self.display_all_employees_by_date,
                    4: self.display_pilots_by_airplane_type_sorted, 9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Name 2. Title 3. Date 4. Airplane"
        return_bool = self.__ui_base_functions.display_menu(
            employee_menu, nav_dict)
        if return_bool == 0:
            return 0
        if return_bool == 9:
            return


    def display_found_employees_by_name(self, employee_list, name):
        ''' display list of employees by input'''

        nav_dict = {9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        while True:
            print("There were more than one ""{}"" found.".format(name))
            print("-" * self.UI_DIVIDER_INT)
            print("|{:<10}{:20}{:15}|".format(
                "Index: ", "Name:", "SSN:"))
            for index, employee in enumerate(employee_list):
                print("|{:02d}{:<8}{:20}{:15}|".format(index+1, "",
                                                       employee.get_name(),
                                                       employee.get_ssn()))
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

    def display_edit_employee(self):
        pass

<<<<<<< HEAD
=======
    def display_one_employee(self, employee):
        print(employee)

>>>>>>> 1057632b16aac15e78cc86e217708d9751fa9300
    def display_select_from_employee_list_menu(self, employee_list):
        nav_dict = {1: employee_list,
                    9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Select employee:"
        return_bool = self.__ui_base_functions.display_menu(
            employee_menu, nav_dict)
        if return_bool == 0:
            return 0
        if return_bool == 9:
            return

<<<<<<< HEAD
    def display_select_from_pilots_list_menu(self, employee_list):
        nav_dict = {1: employee_list, 2: "",
        9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Select employee 2. Filter by airplane type"
        return_bool = self.__ui_base_functions.display_menu(employee_menu, nav_dict)
        if return_bool == 0:
            return 0
        if return_bool == 9:
            return
    
=======
>>>>>>> 1057632b16aac15e78cc86e217708d9751fa9300
    def display_all_employees(self):
        ''' Print the given dictionary of employees '''
        header_flag = "default"
        employee_list = self.__ll_api.get_employee_list_by_name()
        self.__ui_base_functions.print_object_list(
            employee_list, self.__modelAPI, header_flag)
        self.display_select_from_employee_list_menu(employee_list)

    def display_all_employees_by_date(self):
        '''Displays all employees availability on a specific day'''
        # needs input
        header_flag = "date"
        employee_list = self.__ll_api.get_all_employee_list()
        self.__ui_base_functions.print_object_list(
            employee_list, self.__modelAPI, header_flag)
        self.display_select_from_employee_list_menu(employee_list)

    def display_all_employees_by_title(self):
        ''' Print a filtered list of all employees by title '''
        header_flag = "default"
        title = self.__ui_base_functions.get_user_input("title")
        employee_list = self.__ll_api.get_employee_list_by_title(title)
        self.__ui_base_functions.print_object_list(
            employee_list, self.__modelAPI, header_flag)
        if title == "Pilot":
            self.display_select_from_pilots_list_menu(employee_list)
        else:
            self.display_select_from_employee_list_menu(employee_list)

    def display_pilots_by_airplane_type_sorted(self):
        ''' print a sorted list of pilots '''
        header_flag = "aircraft"
        title = "Pilot"
        employee_list = self.__ll_api.get_pilots_sorted_by_airplane_type()
        self.__ui_base_functions.print_object_list(
            employee_list, self.__modelAPI, header_flag)
        self.display_select_from_pilots_list_menu(employee_list)
<<<<<<< HEAD
        
    def get_employee_by_name(self):
        ''' Search for employee instance and print out it's information '''
        name = self.__ui_base_functions.get_user_input("name")
        found_employee_list = self.__ll_api.get_employees_filtered_by_name(name)
=======

    def display_select_from_pilots_list_menu(self, employee_list):
        nav_dict = {1: employee_list, 2: "",
                    9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Select employee 2. Filter by airplane type"
        return_bool = self.__ui_base_functions.display_menu(
            employee_menu, nav_dict)
        if return_bool == 0:
            return 0
        if return_bool == 9:
            return

    def get_employee_by_name(self, name):
        ''' Search for employee instance and print out it's information '''

        found_employee_list = self.__ll_api.get_employees_filtered_by_name(
            name)
>>>>>>> 1057632b16aac15e78cc86e217708d9751fa9300
        if len(found_employee_list) == 1:
            self.__ui_base_functions.print_object(found_employee_list[0])

        else:
            self.display_found_employees_by_name(found_employee_list, name)

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
        address = input("Address: ")
        new_emp.set_address(address)
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
