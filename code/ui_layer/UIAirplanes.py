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
        airplane_menu = "1. Create 2. Display all"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(airplane_menu, " "*(self.UI_DIVIDER_INT - len(airplane_menu) -
                                                    len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-" * self.UI_DIVIDER_INT)

    def create_airplane(self):
        ''' Create an airplane '''
        # 1
        # user input
        name = input("ID: ")
        make = input("Make: ")
        model = input("Model: ")
        total_seats = input("Total seats: ")

    def display_all_airplanes(self):
        ''' Print all airplanes '''
        # 2
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
