class UIVoyages():
    UI_DIVIDER_INT = 124
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    # All menu functions
    
    def get_voyage_sub_menu(self):
        nav_dict = {1: self.create_voyage,
                    2: self.get_all_voyages,
                    3: self.get_voyage_search_menu,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Create 2. Get all 3. Search by"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_voyage_search_menu(self):
        '''Print the search menu of voyage sub menu'''
        nav_dict = {1: self.get_all_voyages_by_destination,
                    2: self.get_all_voyages_by_date,
                    3: self.get_all_empty_voyages,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "Search: 1. Destination 2. Period 3. Empty Voyages"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_voyage_list_menu(self, voyage_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Select voyage"
        return_value = self.__ui_base_functions.print_menu(voyage_menu, nav_dict, voyage_list)
        if return_value != None and return_value != 0:
            return_value = self.get_selected_voyage_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_selected_voyage_menu(self, voyage):
        nav_dict = {1: self.add_crew,
                    2: self.duplicate_voyage,
                    3: self.repeat_voyage,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Add crew 2. Duplicate 3. Repeat"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

    # All list functions
    
    def get_all_voyages(self):
        '''Print the given dictionary of voyages'''
        print("ALL VOYAGES")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_voyages_by_destination(self):
        print("ALL VOYAGES BY DESTINATION")
        destination = self.__ui_base_functions.get_user_input("destination")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_voyages_by_date(self):
        print("ALL VOYAGES BY DATE")
        date = self.__ui_base_functions.get_user_input("date")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_empty_voyages(self):
        print("ALL VOYAGES EMPTY VOYAGES")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)
    
    # All Special functions

    def create_voyage(self):
        print("CREATE VOYAGE GOES HERE!")
        return
    
    def add_crew(self, voyage):
        print("ADD CREW GOES HERE")
        return
    
    def duplicate_voyage(self, voyage):
        print("DUPLICATE VOYAGE GOES HERE")
        return

    def repeat_voyage(self, voyage):
        print("REPEATE VOYAGE GOES HERE")
        return
