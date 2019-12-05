class UIAirplanes():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    def display_airplanes_sub_menu(self):
        ''' Print the airplanes menu '''
        while True:
        
            nav_dict = {1:self.create_airplane, 2:self.display_all_airplanes, 9:self.__ui_base_functions.back,0:self.__ui_base_functions.home}
            airplane_menu = "1. Create 2. Display all"
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(airplane_menu, " "*(self.UI_DIVIDER_INT - len(airplane_menu) -
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

    def create_airplane(self):
        ''' Create an airplane '''
        # 1
        # user input
        make  = input("Make: ")
        model =  input("Model: ")
        insignia = input("Insignia: ").upper()
        new_airplane = self.__modelAPI.get_model("Airplane")
        new_airplane.set_make(make)
        new_airplane.set_model(model)
        new_airplane.set_name(insignia)
        self.__ll_api.create_airplane(new_airplane)



    def display_all_airplanes(self):
        ''' Print all airplanes '''
        # 2
        while True:
            nav_dict = {9: self.__ui_base_functions.back, 0: self.__ui_base_functions.home}
            print("-" * self.UI_DIVIDER_INT)
            print("{:11}{:11}{:12}{:17}{:11}{:17}{:17}{:12}".format(
                "ID:", "Make:", "Model:", "Total seats:", "Status:", "Destination:", "Flight number:", "Date available:"))
            print("-" * self.UI_DIVIDER_INT)
            airplanes_list = self.__ll_api.get_all_airplanes_list()
            for airplanes in airplanes_list[1:]:
                print("{:11}{:11}{:12}{:17}{:11}{:17}{:17}{:12}".format(airplanes.get_name(),
                                                                        airplanes.get_make(),
                                                                        airplanes.get_model(),
                                                                        airplanes.get_max_seats(),
                                                                        "Missing status",
                                                                        "Missing destination",
                                                                        "Missing flight_number",
                                                                        "Missing date_available"))
            choice = int(input("Input: "))
            try:
                choice =  nav_dict[choice]()
                if choice == 0:
                    return 0
                if choice == 9:
                    return
            except KeyError:
                print("Invalid input! try again")
