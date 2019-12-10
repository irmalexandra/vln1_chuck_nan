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
        ''' Print the search menu of voyage sub menu '''
        nav_dict = {1: self.get_all_voyages_by_airport,
                    2: self.get_all_voyages_by_date,
                    3: self.get_all_empty_voyages,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "Search by: 1. Airport 2. Period 3. Empty Voyages"
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
            if return_value.get_airplane_insignia() == ".":
                return_value = self.get_selected_voyage_no_airplane_menu(return_value)
            elif return_value.get_captain_ssn() == ".":
                return_value = self.get_selected_voyage_empty_menu(return_value)
            else:
                return_value = self.get_selected_voyage_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_airplane_list_menu(self, airplane_list, voyage):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Select airplane"
        return_value = self.__ui_base_functions.print_menu(voyage_menu, nav_dict, airplane_list)
        if return_value != None and return_value != 0:
            voyage.set_airplane_insignia(return_value.get_insignia())
            self.__ui_base_functions.print_airplane_added_results(return_value)
            
        return self.__ui_base_functions.check_return_value(return_value)

    def get_selected_voyage_no_airplane_menu(self, voyage):
        nav_dict = {1: self.duplicate_voyage,
                    2: self.repeat_voyage,
                    3: self.get_all_airplanes,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Duplicate 2. Repeat 3. Add Airplane"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict, voyage)
        if return_value != None and return_value != 0:
            if voyage.get_airplane_insignia() != ".":
                return_value = self.get_selected_voyage_empty_menu(voyage)
        return self.__ui_base_functions.check_return_value(return_value)
    
    def get_selected_voyage_menu(self, voyage):
        nav_dict = {1: self.duplicate_voyage,
                    2: self.repeat_voyage,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Duplicate 2. Repeat"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_selected_voyage_empty_menu(self, voyage):
        nav_dict = {1: self.duplicate_voyage,
                    2: self.repeat_voyage,
                    3: self.get_add_crew_voyage_menu,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Duplicate 2. Repeat 3. Add Crew"
        return_value = self.__ui_base_functions.print_menu(
            voyage_menu, nav_dict, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_add_crew_voyage_menu(self, voyage):
        nav_dict = {1: self.get_all_captains_by_airplane_and_availability,
                    2: self.get_all_copilots_by_airplane_and_availability,
                    3: self.get_all_fsm_by_availability,
                    4: self.get_all_flight_attendants_by_availability,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        edit_menu = "Add: 1. Captain 2. Co-Pilot 3. Flight Service Manager 4. Flight Attendant"
        return_value = self.__ui_base_functions.print_menu(
            edit_menu, nav_dict, voyage)
        if return_value != None and return_value != 0:
            return_value = self.get_select_from_add_crew_list_menu(return_value, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_add_crew_list_menu(self, crew_list, voyage):
        nav_dict = {1: self.__ui_base_functions.select_from_crew_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        voyage_menu = "1. Select crew member"
        return_value = self.__ui_base_functions.print_menu(voyage_menu, nav_dict, crew_list)
        if return_value != None and return_value != 0:
            self.__ui_base_functions.print_add_crew_results(return_value)
            return_value = self.__ll_api.add_crew_member_to_voyage()# MUNA AÐ ADD CREW SEINNA
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_destination_list_menu(self, employee_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Select destination"
        return_value = self.__ui_base_functions.print_menu(employee_menu, nav_dict, employee_list)
        if return_value != None and return_value != 0:
            return_value = self.get_selected_employee_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)

    # All list functions

    def get_all_airplanes(self, voyage):
        header_flag = "default"
        airplane_list = self.__ll_api.get_all_available_airplane_list(voyage)
        return_value = self.__ui_base_functions.print_model_list(
            airplane_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_list_menu(airplane_list, voyage)
        return self.__ui_base_functions.check_return_value(return_value)
    
    def get_all_voyages(self):
        '''Print the given dictionary of voyages'''
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_voyages_by_airport(self):
        airport = self.__ui_base_functions.get_user_input("airport")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list_by_airport(airport)
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_voyages_by_date(self):
        start_date = self.__ui_base_functions.get_user_input("start date DD-MM-YYYY")
        end_date = self.__ui_base_functions.get_user_input("end date DD-MM-YYYY")
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_voyage_list_by_period_list(start_date, end_date)
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_empty_voyages(self):
        header_flag = "default"
        voyage_list = self.__ll_api.get_all_empty_voyage_list()
        return_value = self.__ui_base_functions.print_model_list(
            voyage_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_voyage_list_menu(voyage_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_captains_by_airplane_and_availability(self, voyage):
        '''Print the given dictionary of voyages'''
        header_flag = "aircraft"
        rank = "Captain"
        crew_list = self.__ll_api.get_filtered_employee_list_for_voyage(rank,voyage)
        return_value = self.__ui_base_functions.print_model_list(
            crew_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_add_crew_list_menu(crew_list, voyage)
        return self.__ui_base_functions.check_return_value(return_value)
    
    def get_all_copilots_by_airplane_and_availability(self, voyage):
        '''Print the given dictionary of voyages'''
        header_flag = "aircraft"
        rank = "Copilot"
        crew_list = self.__ll_api.get_filtered_employee_list_for_voyage(rank,voyage)
        return_value = self.__ui_base_functions.print_model_list(
            crew_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_add_crew_list_menu(crew_list, voyage)
        return self.__ui_base_functions.check_return_value(return_value)
    
    def get_all_fsm_by_availability(self, voyage):
        '''Print the given dictionary of voyages'''
        header_flag = "default"
        rank = "Flight Service Manager"
        crew_list = self.__ll_api.get_filtered_employee_list_for_voyage(rank,voyage)
        return_value = self.__ui_base_functions.print_model_list(
            crew_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_add_crew_list_menu(crew_list, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_flight_attendants_by_availability(self, voyage):
        '''Print the given dictionary of voyages'''
        header_flag = "default"
        rank = "Flight Attendant"
        crew_list = self.__ll_api.get_filtered_employee_list_for_voyage(rank,voyage)
        return_value = self.__ui_base_functions.print_model_list(
            crew_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_add_crew_list_menu(crew_list, voyage)
        return self.__ui_base_functions.check_return_value(return_value)

        
    
    # All Special functions

    def create_voyage(self):
        header_flag = "default"
        destination_list = self.__ll_api.get_all_destination_list()
        return_value = self.__ui_base_functions.print_model_list(destination_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_destination_list_menu(return_value)
        if return_value != None and return_value != 0:
            new_date = self.__ui_base_functions.get_user_input("new date ""(dd-mm-yyyy)"": ")
            new_time = self.__ui_base_functions.get_user_input("new time ""(hh:mm:ss)"": ")
            if self.__ll_api.create_voyage(return_value, new_date, new_time):
                self.__ui_base_functions.print_create_voyage_results(return_value, new_date, new_time)
            else:
                print("no bueno")
                

        
        
       

    
    def duplicate_voyage(self, voyage):

        new_date = self.__ui_base_functions.get_user_input("new date ""(dd-mm-yyyy)"": ")
        new_time = self.__ui_base_functions.get_user_input("new time ""(hh:mm:ss)"": ")
        
        return_value = self.__ll_api.duplicate_voyage(voyage, new_date, new_time)
        if return_value == True:
            print("Voyage duplication successful!")
        else:
            print("Incorrect date/time format")
        return self.__ui_base_functions.check_return_value(return_value)
    
    def repeat_voyage(self, voyage):
        interval = self.__ui_base_functions.get_user_input("repeat inverval: ")
        end_date = self.__ui_base_functions.get_user_input("end date ""(dd-mm-yyyy)"": ")
        
        return_value = self.__ll_api.repeat_voyage(voyage, interval, end_date)
        if return_value == True:
            print("Creation of reccuring voyage successful!")
        else:
            print("Incorrect date format or interval format")
        return self.__ui_base_functions.check_return_value(return_value)
