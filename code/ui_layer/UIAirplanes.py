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
        existing_airplane_types = self.__ll_api.pull_airplane_types()
        existing_airplane_types_list = [x.split(",") for x in existing_airplane_types]  
        print("Supported airplanes: ")
        for number, plane in enumerate(existing_airplane_types_list):
            print(number + 1, plane[1] + plane[2])

        
        picked_airplane = input("Pick plane: ")
        if picked_airplane == "1":
            make = existing_airplane_types_list[0][self.MAKE]
            model = existing_airplane_types_list[0][self.MODEL]
        elif picked_airplane == "2":
            make = existing_airplane_types_list[1][self.MAKE]
            model = existing_airplane_types_list[1][self.MODEL]
        elif picked_airplane == "3":
            make = existing_airplane_types_list[2][self.MAKE]
            model = existing_airplane_types_list[2][self.MODEL]
        
        insignia = "TF-" + input("Insignia: (must be 3 letters) ").upper()
        
        new_airplane = self.__modelAPI.get_model("Airplane")
        new_airplane.set_make(make)
        new_airplane.set_model(model)
        new_airplane.set_name(insignia)
        make_bool, model_bool, airplane = self.__ll_api.create_airplane(new_airplane, existing_airplane_types)
        print("Make is ", make_bool, "model is ", model_bool)
        if make_bool == True and model_bool == True:
            print(airplane, "\n Created succesfully!")
        elif make_bool == False  and model_bool == None:
            print("Invalid input", model)
        elif make_bool == None and model_bool == False :
            print("Invalid input", make)
        else:
            print("Both",make,"and",model,"Invalid")




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
