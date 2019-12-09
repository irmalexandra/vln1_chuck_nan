class UIDestinations():
    RETURN_MENU_STR = "9. Return 0. Home"
    EDIT_FEEDBACK_TPL = ("name", "number")

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    #All menu functions

    def get_destination_sub_menu(self):
        nav_dict = {1: self.create_destination,
                    2: self.get_all_destinations,
                    3: self.get_destination_search_menu,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        destination_menu = "1. Create 2. Get all 3. Search by"
        return_value = self.__ui_base_functions.print_menu(
            destination_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_destination_search_menu(self):
        '''Print the search menu of employee sub menu'''
        nav_dict = {1: self.get_all_destinations_by_country,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        destination_menu = "1. Country name"
        return_value = self.__ui_base_functions.print_menu(
            destination_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_selected_destination_menu(self, employee):

        nav_dict = {1: self.change_contact_name,
                    2: self.change_contact_number,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        destination_menu = "1. Change Name 2. Change Phone Number"
        return_value = self.__ui_base_functions.print_menu(
            destination_menu, nav_dict, employee)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_destination_list_menu(self, employee_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        destination_menu = "1. Select destination:"
        return_value = self.__ui_base_functions.print_menu(destination_menu, nav_dict, employee_list)
        if return_value != None and return_value != 0:
            return_value = self.get_selected_destination_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    #All list functions

    def get_all_destinations(self):
        '''Print the given dictionary of destinations'''
        header_flag = "default"
        destination_list = self.__ll_api.get_all_destination_list()
        return_value = self.__ui_base_functions.print_model_list(
            destination_list, self.__modelAPI, header_flag)
        return_value = self.get_select_from_destination_list_menu(destination_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_destinations_by_country(self):
        '''Search for distination instance and returns a list'''
        header_flag = "default"
        country = self.__ui_base_functions.get_user_input("country")
        found_destination_list = self.__ll_api.get_destination_list_by_country(
            country)
        return_value = self.__ui_base_functions.print_model_list(found_destination_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_destination_list_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)
 
    # Specific functions
    
    def create_destination(self):
        print("CREATE DESTINATION GOES HERE!")
    
    def change_contact_name(self, destination):
        print("CHANGE NAME GOES HERE!")
        string = self.__ui_base_functions.get_user_input("contact name")

    def change_contact_number(self, destination):
        print("CHANGE CONTACT NUMBER GOES HERE!")
        number = self.__ui_base_functions.get_user_input("contact name")
        
