class UIAirplanes():
    UI_DIVIDER_INT = 124
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2
    MAKE = 1
    MODEL = 2

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    
    
    def get_airplanes_sub_menu(self):
            nav_dict = {1:self.create_airplane,
                        2:self.display_all_airplanes,
                        9:self.__ui_base_functions.back,
                        0:self.__ui_base_functions.home}
            airplane_menu = "1. Create 2. Get all"
            return_value = self.__ui_base_functions.print_menu(airplane_menu,nav_dict)
            return self.__ui_base_functions.check_return_value(return_value)

    def get_edit_airplane_menu(self):
        print("EDIT GOES HERE")

    def get_selected_airplane_menu(self, airplane):
        nav_dict = {1: self.get_edit_airplane_menu, 9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
        airplane_menu = "1. Edit airplane"
        return_value =  self.__ui_base_functions.print_menu(airplane_menu,nav_dict,airplane)
        return self.__ui_base_functions.check_return_value(return_value)


    def get_select_from_airplane_list_menu(self,airplanes_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        airplane_menu = "1. Select airplane"
        return_value = self.__ui_base_functions.print_menu(airplane_menu,nav_dict,airplanes_list)
        if return_value != None and return_value != 0:
            return_value = self.get_selected_airplane_menu(return_value)
        return self.__ui_base_functions.check_return_value(return_value)



    def display_all_airplanes(self):
        header_flag = "default"
        airplanes_list = self.__ll_api.get_all_airplane_list()
        return_value = self.__ui_base_functions.print_model_list(airplanes_list,self.__modelAPI,header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_list_menu(airplanes_list)
        return self.__ui_base_functions.check_return_value(return_value)
    

    def create_airplane(self):
        '''Create an airplane'''
        # 1
        # user input
        existing_airplane_types_list = self.__ll_api.get_airplane_type_list()
        print("Supported airplanes: ")
        for number, plane in enumerate(existing_airplane_types_list):
            print(number + 1, plane.get_make() + plane.get_model())

        
        picked_airplane = input("Pick an airplane type: ")
        if picked_airplane == "1":
            make = existing_airplane_types_list[0].get_make()
            model = existing_airplane_types_list[0].get_model()
        elif picked_airplane == "2":
            make = existing_airplane_types_list[1].get_make()
            model = existing_airplane_types_list[1].get_model()
        elif picked_airplane == "3":
            make = existing_airplane_types_list[2].get_make()
            model = existing_airplane_types_list[2].get_model()
        else:
            print("Input: {} invalid".format(picked_airplane))
            return self.create_airplane()
        insignia = "TF-" + input("Insignia (must be 3 letters): TF-").upper()
        
        new_airplane = self.__modelAPI.get_model("Airplane")
        new_airplane.set_make(make)
        new_airplane.set_model(model)
        check = new_airplane.set_insignia(insignia)
        if check:
            if self.__ll_api.create_airplane(new_airplane, existing_airplane_types_list,insignia):
                print("\nAirplane created!\n{}".format(new_airplane))
            else:
                print("\n{}\nAlready exists!".format(new_airplane.get_insignia()))
        else:
            print("\nInvalid insignia {}\n".format(insignia))


    # def display_all_airplanes_old(self):
    #     ''' Print all airplanes '''
    #     # 2
    #     while True:
    #         nav_dict = {9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
    #         print("-" * self.UI_DIVIDER_INT)
    #         print("{:11}{:11}{:12}{:17}{:11}{:17}{:17}{:12}".format(
    #             "ID:", "Make:", "Model:", "Total seats:", "Status:", "Destination:", "Flight number:", "Date available:"))
    #         print("-" * self.UI_DIVIDER_INT)
    #         airplanes_list = self.__ll_api.get_all_airplanes_list()
    #         for airplanes in airplanes_list[1:]:
    #             print("{:11}{:11}{:12}{:17}{:11}{:17}{:17}{:12}".format(airplanes.get_name(),
    #                                                                     airplanes.get_make(),
    #                                                                     airplanes.get_model(),
    #                                                                     airplanes.get_max_seats(),
    #                                                                     "Missing status",
    #                                                                     "Missing destination",
    #                                                                     "Missing flight_number",
    #                                                                     "Missing date_available"))
    #         choice = int(input("Input: "))
            
    #         try:
    #             choice =  nav_dict[choice]()
    #             if choice == 0:
    #                 return 0
    #             if choice == 9:
    #                 return
    #         except KeyError:
    #             print("Invalid input! try again")



    # def display_airplanes_sub_menu(self):
    #     ''' Print the airplanes menu '''
    #     while True:
        
    #         nav_dict = {1:self.create_airplane, 2:self.display_all_airplanes, 9:self.__ui_base_functions.back,0:self.__ui_base_functions.home}
    #         airplane_menu = "1. Create 2. Display all"
    #         print("-" * self.UI_DIVIDER_INT)
    #         print("|{}{}{}|".format(airplane_menu, " "*(self.UI_DIVIDER_INT - len(airplane_menu) -
    #                                                     len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
    #         print("-" * self.UI_DIVIDER_INT)
    #         choice = int(input("Input: "))
    #         try:
    #             choice =  nav_dict[choice]()
    #             if choice == 0:
    #                 return 0
    #             if choice == 9:
    #                 return
    #         except KeyError:
    #             print("Invalid input! try again")
