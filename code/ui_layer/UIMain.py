from logic_layer.LLAPI import LLAPI
from models.ModelAPI import ModelAPI
from ui_layer import UIBaseFunctions
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees
from ui_layer.UIVoyages import UIVoyages
from ui_layer.UIDestinations import UIDestinations
from ui_layer.UIAirplanes import UIAirplanes

import string


class UIMain():

    LINE_LEN = 88
    T_LEN = 18
    TRUE_LEN = LINE_LEN + 2 * T_LEN
    UI_DIVIDER_INT = TRUE_LEN
    distinguisher = "{}\n{}\n\n".format("_"*TRUE_LEN, "_"*TRUE_LEN)
    RETURN_MENU_STR = "0. Exit"
    DEVIATION_INT = 2

    def __init__(self):
        self.__LLAPI = LLAPI()
        self.__ui_base_functions = UIBaseFunctions()
        self.__modelAPI = ModelAPI()
        self.__ui_employees = UIEmployees(
            self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.__ui_voyages = UIVoyages(
            self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.__ui_destinations = UIDestinations(
            self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.__ui_airplanes = UIAirplanes(
            self.__LLAPI, self.__modelAPI, self.__ui_base_functions)

    def print_nan_airlines(self):
        print(UIMain.distinguisher)
        print(self.T_LEN*" " + "███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗")
        print(self.T_LEN*" " + "████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝")
        print(self.T_LEN*" " + "██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗")
        print(self.T_LEN*" " + "██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║")
        print(self.T_LEN*" " + "██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║")
        print(self.T_LEN*" " + "╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
        print(UIMain.distinguisher, end="")

    def display_main_menu(self):
        while True:
            nav_dict = {1: self.__ui_employees.display_employee_sub_menu, 2: self.__ui_voyages.display_voyage_sub_menu,
                        3: self.__ui_destinations.display_destination_sub_menu, 4: self.__ui_airplanes.display_airplanes_sub_menu, 0: self.__ui_base_functions.exit_program()}
            self.print_nan_airlines()
            main_menu = "1. Employees 2. Voyages 3. Destinations 4. Airplanes"
            #print("{}{}".format(true_menu, " " * (UIMain.TRUE_LEN - len(true_menu)-1)))
            print("-"*self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(main_menu, " "*(self.UI_DIVIDER_INT -
                                                    len(main_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
            print("-"*self.UI_DIVIDER_INT)
            choice = int(input("Input: "))
            try:
                choice = nav_dict[choice]()

            except KeyError:
                print("Invalid input! try again")
