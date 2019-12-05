class UIVoyages():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    def display_voyage_sub_menu(self):
        ''' Print the destination menu '''
        while True:
        
            nav_dict = {1: self.create_voyage, 2: self.display_all_voyages, 3: self.voyages_search_menu, 9:self.__ui_base_functions.back,0:self.__ui_base_functions.home}
            voyage_menu = "1. Create 2. All 3. Search"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(voyage_menu, " "*(self.UI_DIVIDER_INT - len(voyage_menu) -
                                                    len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice =  nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def create_voyage(self):
        ''' Create a voyage '''
        # 1 
        destination = input("Destination: ")
        airplane = input("Airplane: ")
        departure_date = input("Departure date: ")
        departure_time = input("Departure time: ")
        return_date = input("Return date: ")
        return_time = input("Return time: ")
        departure_flight_number = input("Departure flight number: ")
        return_flight_number = input("Return flight number: ")

    def display_all_voyages(self):
        ''' Print all voyages '''
        # 2
        while True:
        
            nav_dict = {9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
            print("-" * self.UI_DIVIDER_INT)
            print("{:15}{:11}{:27}{:27}{:27}{:27}{:17}".format(
                "Destination:", "Airplane:", "Departure date and time:", "Return date and time:", "Departure flight number:", "Return flight number:", "Status"))
            print("-" * self.UI_DIVIDER_INT)
            voyages_list = self.__ll_api.get_all_voyages_list()
            for voyages in voyages_list[1:]:
                print("{:15}{:11}{:27}{:27}{:27}{:27}{:17}".format(voyages.get_return_flight_departing_from(),
                                                                voyages.get_aircraft_id(),
                                                                voyages.get_departing_flight_departure_date(),
                                                                voyages.get_return_flight_arrival_date(),
                                                                voyages.get_departing_flight_num(),
                                                                voyages.get_return_flight_num(),
                                                                "Missing status"))
            choice = int(input("Input: "))
            try:
                choice =  nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")
        

    def display_one_voyage(self):
        ''' Search for a voyage and print the information '''
        # 3
        # need to implement input
        print("Destination:")
        print("Airplane:")
        print("Departure date and time:")
        print("Return date and time:")
        print("Departure flight number:")
        print("Return flight number:")
        print("Status:")

        print("Pilot: ")
        print("Co-Pilot: ")
        print("Flight Service Manager: ")
        print("Cabin Crew: ")

        print("Person 1: ")
        print("Person 2: ")
        print("Person 3: ")

    def voyages_search_menu(self):
        ''' Print the search menu for the voyages '''
        while True:
        
            nav_dict = {1: self.get_voyages_by_destination, 2: self.get_voyages_by_period, 3: self.get_empty_voyages, 9:self.__ui_base_functions.back,0:self.__ui_base_functions.home}
            search_menu = "1. Destination 2. Period 3. Empty Voyages"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(search_menu, " "*(self.UI_DIVIDER_INT -
                                                    len(search_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice =  nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def voyages_search_sub_sub_menu(self):
        ''' Print the search menu for the voyages '''
        while True:
        
            nav_dict = {9:self.__ui_base_functions.back,0:self.__ui_base_functions.home}
            search_menu = "1. Add Crew 2. Duplicate 3. Repeat"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(search_menu, " "*(self.UI_DIVIDER_INT -
                                                    len(search_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
            print("-" * self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice =  nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")

    def add_crew(self):
        pilot = input("Select pilot: ")
        co_pilot = input("Select Co-Pilot: ")
        flight_service_management = ("Select flight service manager: ")
        add_crew = ("Select flight attendant (input 1 when done): ")

    def duplicate_voyage(self):
        pass

    def repeat_voyage(self):
        pass

    def get_voyages_by_destination(self):
        print("voyages by destination not yet implemented")
        pass
    
    def get_voyages_by_period(self):
        print("voyages by period not yet implemented")
        pass

    def get_empty_voyages(self):
        print("empty voyages not yet implemented")
        pass