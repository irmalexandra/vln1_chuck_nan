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
        destination_menu = "1. Create 2. get all 3. Search by"
        return_value = self.__ui_base_functions.print_menu(
            destination_menu, nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_destination_search_menu(self):
        '''Print the search menu of employee sub menu'''
        nav_dict = {1: self.get_destination_by_airport,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        destination_menu = "1. Airport name"
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

    # Specific functions

    def get_destination_by_airport(self):
        pass
    
    def create_destination(self):
        pass

    # def display_destination_sub_menu(self):
    #     ''' Print the destination menu '''
    #     while True:

    #         nav_dict = {1: self.create_destination, 2: self.display_all_destinations,
    #                     3: self.display_search_by_name, 9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
    #         destination_menu = "1. Create 2. Display all 3. Search by name"
    #         print("-" * self.UI_DIVIDER_INT)
    #         print("|{}{}{}|".format(destination_menu, " "*(self.UI_DIVIDER_INT - len(destination_menu) -
    #                                                        len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
    #         print("-" * self.UI_DIVIDER_INT)
    #         choice = int(input("Input: "))
    #         try:
    #             choice = nav_dict[choice]()
    #             if choice == 0:
    #                 return 0
    #             if choice == 9:
    #                 return
    #         except KeyError:
    #             print("Invalid input! try again")

    # def create_destination(self):
    #     ''' Create a destination '''
    #     # 1
    #     # user input
    #     country = input("Country: ")
    #     airport = input("Airport: ")
    #     flight_time = input("Flight time (h): ")
    #     distance = input("Distance (km): ")
    #     contact_name = input("Contact name: ")
    #     contact_number = input("Contact number: ")

    # def display_search_by_name(self):
    #     airport = input("Airport name: ")
    #     destination = self.__ll_api.get_one_destination(airport)
    #     if destination == None:
    #         print("Airport not found.")
    #     else:
    #         self.display_one_destination(destination)

    # def display_create_destination_header(self):
    #     counter = 1
    #     header = "Create Destination "
    #     print("{}{}".format(header, "(" + counter + "/6)"))

    # def display_all_destinations(self):
    #     ''' Print all destinations '''
    #     # 2
    #     while True:

    #         nav_dict = {9: self.__ui_base_functions.back,
    #                     0: self.__ui_base_functions.home}
    #         print("-" * self.UI_DIVIDER_INT)
    #         print("{:19}{:15}{:17}{:15}{:20}{:10}".format(
    #             "Country:", "Airport:", "Flight time:", "Distance:", "Contact name:", "Contact number:"))
    #         print("-" * self.UI_DIVIDER_INT)
    #         destinations_list = self.__ll_api.get_all_destinations_list()
    #         for destinations in destinations_list[1:]:
    #             print("{:19}{:15}{:17}{:15}{:20}{:10}".format(destinations.get_country(),
    #                                                           destinations.get_airport(),
    #                                                           destinations.get_flight_time(),
    #                                                           destinations.get_distance(),
    #                                                           destinations.get_contact_name(),
    #                                                           destinations.get_contact_number()))
    #         choice = int(input("Input: "))
    #         try:
    #             choice = nav_dict[choice]()
    #             if choice == 0:
    #                 return 0
    #             if choice == 9:
    #                 return
    #         except KeyError:
    #             print("Invalid input! try again")

    # def display_one_destination(self, destination):
    #     ''' Search for a destination and print the information '''

    #     destination_menu = "1. Change Name 2. Change Phone Number"
    #     while True:

    #         nav_dict = {1: self.change_contact, 2: self.change_contact_number, 9: self.__ui_base_functions.back,
    #                     0: self.__ui_base_functions.home}
    #         print("-" * self.UI_DIVIDER_INT)
    #         print(destination)
    #         print("-" * self.UI_DIVIDER_INT)
    #         print("|{}{}{}|".format(destination_menu, " "*(self.UI_DIVIDER_INT - len(destination_menu) -
    #                                                        len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
    #         print("-" * self.UI_DIVIDER_INT)
    #         choice = int(input("Input: "))
    #         try:
    #             choice = nav_dict[choice]()
    #             if choice == 0:
    #                 return 0
    #             if choice == 9:
    #                 return
    #             if self.__ll_api.edit_destination(destination, choice):
    #                 print("Contact {} successful1y changed to {}".format(
    #                     self.EDIT_FEEDBACK_TPL[choice[0]], choice[1]))
    #             else:
    #                 print("Invalid input!")

    #         except KeyError:
    #             print("Invalid input! try again")

    def change_contact_name(self):
        string = input("Enter new contact name: ")
        return (0, string)

    def change_contact_number(self):
        number = input("Enter new contact number: ")
        return (1, number)
