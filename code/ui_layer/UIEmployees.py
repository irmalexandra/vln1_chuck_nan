class UIEmployees():
    UI_DIVIDER_INT = 124
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2
    WALL = "|"

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    #All menu functions
    
    def get_employee_sub_menu(self):
        nav_dict = {1: self.create_employee_sub_menu,
                    2: self.get_all_employees,
                    3: self.get_employee_search_menu,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Create 2. Get all 3. Search by"
        return_value = self.__ui_base_functions.print_menu(
            employee_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_employee_search_menu(self):
        '''Print the search menu of employee sub menu'''
        nav_dict = {1: self.get_all_employees_by_name,
                    2: self.get_all_employees_by_title,
                    3: self.get_all_employees_by_date,
                    4: self.get_pilots_by_airplane_type_sorted,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Name 2. Title 3. Date 4. Airplane"
        return_value = self.__ui_base_functions.print_menu(
            employee_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def create_employee_sub_menu(self):
        nav_dict = {1: self.create_pilot,
                    2: self.create_cabin_crew,
                    3: self.get_employee_search_menu,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Pilot 2. Cabin Crew"
        return_value = self.__ui_base_functions.print_menu(
            employee_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_selected_employee_menu(self, employee):
        if employee.get_title() == "Pilot":
            nav_dict = {1: self.get_edit_employee_menu,
                        2: self.get_work_schedule,
                        3: self.change_pilot_licence,
                        9: self.__ui_base_functions.back,
                        0: self.__ui_base_functions.home}
            employee_menu = "1. Edit Employee 2. Work Schedule 3. Change Licence"
            return_value = self.__ui_base_functions.print_menu(
                employee_menu, nav_dict, employee)
            return self.__ui_base_functions.check_return_value(return_value)
        else:
            nav_dict = {1: self.get_edit_employee_menu,
                        2: self.get_work_schedule,
                        9: self.__ui_base_functions.back,
                        0: self.__ui_base_functions.home}
            employee_menu = "1. Edit Employee 2. Work Schedule"
            return_value = self.__ui_base_functions.print_menu(
                employee_menu, nav_dict,  employee)
            return self.__ui_base_functions.check_return_value(return_value)

    def get_edit_employee_menu(self, employee):
        nav_dict = employee.get_edit_dict()
        nav_dict[9] = self.__ui_base_functions.back
        nav_dict[0] = self.__ui_base_functions.home
        edit_order_list = employee.get_edit_order_list()
        edit_menu = "Change: 1. Address 2. Home Number 3. Mobile Number 4. Title 5. Rank"
        return_value = self.__ui_base_functions.print_edit_model_menu(
            edit_menu, nav_dict, employee, edit_order_list, self.__ll_api)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_employee_list_menu(self, employee_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Select employee"
        return_value = self.__ui_base_functions.print_menu(employee_menu, nav_dict, employee_list)
        if return_value != None and return_value != 0:
            return_value = self.get_selected_employee_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_airplane_type_list_menu(self, airplane_type_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Select Airplane Type"
        return_value = self.__ui_base_functions.print_menu(employee_menu, nav_dict, airplane_type_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_pilots_list_menu(self, employee_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    2: self.get_pilots_filtered_by_airplane_type,
                    9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        employee_menu = "1. Select employee 2. Filter by airplane type"
        return_value = self.__ui_base_functions.print_menu(
            employee_menu, nav_dict, employee_list)
        if return_value != None and return_value != 0 and return_value != 9:
            return_value = self.get_selected_employee_menu(return_value)
        if return_value == None:
            return_value = 9
        return self.__ui_base_functions.check_return_value(return_value)

    # All list functions

    def get_all_employees(self):
        '''Print the given dictionary of employees'''
        header_flag = "default"
        employee_list = self.__ll_api.get_employee_list_by_name()
        return_value = self.__ui_base_functions.print_model_list(
            employee_list, self.__modelAPI, header_flag)
        return_value = self.get_select_from_employee_list_menu(employee_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_employees_by_date(self):
        '''Gets all employees availability on a specific day'''
        # needs input
        header_flag = "date"
        employee_list = self.__ll_api.get_all_employee_list()
        return_value = self.__ui_base_functions.print_model_list(
            employee_list, self.__modelAPI, header_flag)
        return_value = self.get_select_from_employee_list_menu(employee_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_employees_by_title(self):
        '''Print a filtered list of all employees by title'''
        title = self.__ui_base_functions.get_user_input("title")
        if title == "Pilot":
            header_flag = "aircraft"
        else:
            header_flag = "aircraft"
        employee_list = self.__ll_api.get_employee_list_by_title(title)
        return_value = self.__ui_base_functions.print_model_list(employee_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            if title == "Pilot":
                return_value = self.get_select_from_pilots_list_menu(employee_list)
            else:
                return_value = self.get_select_from_employee_list_menu(employee_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_employees_by_name(self):
        '''Search for employee instance and print out it's information'''
        header_flag = "default"
        name = self.__ui_base_functions.get_user_input("name")
        found_employee_list = self.__ll_api.get_employee_list_filtered_by_name(
            name)
        return_value = self.__ui_base_functions.print_model_list(found_employee_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_employee_list_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_pilots_by_airplane_type_sorted(self, employee_list = []):
        '''Print a sorted list of pilots'''
        header_flag = "aircraft"
        employee_list = self.__ll_api.get_pilot_list_sorted_by_airplane_type()
        return_value = self.__ui_base_functions.print_model_list(employee_list, self.__modelAPI, header_flag)
        return_value = self.get_select_from_pilots_list_menu(employee_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_pilots_filtered_by_airplane_type(self, employee_list = []):
        header_flag = "aircraft"
        airplane = self.__ui_base_functions.get_user_input("airplane name")
        employee_list = self.__ll_api.get_pilot_list_filtered_by_airplane_type(airplane)
        return_value = self.__ui_base_functions.print_model_list(employee_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_pilots_list_menu(employee_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_work_schedule(self, employee):
        employee_work_schedule = self.__ll_api.get_work_schedule_list(employee)
        header_flag = "default"
        return_value = self.__ui_base_functions.print_model_list(employee_work_schedule, self.__modelAPI, header_flag)
        return_value = self.__ui_base_functions.check_return_value(return_value)

    # Specific functions

    def create_pilot(self):
        new_emp = self.__modelAPI.get_model("Employee")
        new_emp.set_title("Pilot")
        self.change_pilot_licence(new_emp)
        create_order_list, creation_dict = new_emp.get_creation_process()
        for attribute in create_order_list:
            while True:
                new_attribute = self.__ui_base_functions.get_user_input(attribute)
            
                if creation_dict[attribute](new_attribute):
                    break
        self.__ll_api.create_employee(new_emp)
        self.__ui_base_functions.print_model(new_emp)
        self.__ui_base_functions.print_create_employee_results(new_emp)
    
    def create_cabin_crew(self):
        new_emp = self.__modelAPI.get_model("Employee")
        new_emp.set_title("Cabincrew")
        create_order_list, creation_dict = new_emp.get_creation_process()
        for attribute in create_order_list:
            while True:
                new_attribute = self.__ui_base_functions.get_user_input(attribute)
            
                if creation_dict[attribute](new_attribute):
                    break
                else:
                    print("Error, {} invalid!".format(attribute))
        self.__ll_api.create_employee(new_emp)
        self.__ui_base_functions.print_model(new_emp)
        self.__ui_base_functions.print_create_employee_results(new_emp)
   
    def change_pilot_licence(self, employee):
        header_flag = "default"
        airplane_type_list = self.__ll_api.get_airplane_type_list()
        return_value = self.__ui_base_functions.print_model_list(airplane_type_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_type_list_menu(return_value)
        if return_value != None and return_value != 0:
            return_value = self.__ui_base_functions.print_airplane_licence_results(return_value)
            employee.set_licence(return_value.get_plane_type_id())   
            if employee.get_name() != "":
                self.__ll_api.overwrite_all_models(employee)     
        
    
