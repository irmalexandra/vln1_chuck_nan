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
    T_LEN = 8
    TRUE_LEN = LINE_LEN + 2 * T_LEN
    UI_DIVIDER_INT = TRUE_LEN
    distinguisher = "{}\n{}\n\n".format("_"*TRUE_LEN, "_"*TRUE_LEN)
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self):
        self.__LLAPI = LLAPI()
        self.__ui_base_functions = UIBaseFunctions()
        self.__modelAPI = ModelAPI()
        self.ui__employees = UIEmployees(self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.ui__voyages = UIVoyages(self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.ui__destinations = UIDestinations(self.__LLAPI, self.__modelAPI, self.__ui_base_functions)
        self.ui__airplanes = UIAirplanes(self.__LLAPI, self.__modelAPI, self.__ui_base_functions)

    def print_nan_airlines(self):
        print(UIMain.distinguisher)
        print("\t███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗")
        print("\t████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝")
        print("\t██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗")
        print("\t██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║")
        print("\t██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║")
        print("\t╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
        print(UIMain.distinguisher, end="")

    def display_main_menu(self):
        nav_dict = {1:self.ui__employees.display_employee_sub_menu,2:"",3:"",4:"",9:"",0:""}
        self.print_nan_airlines()
        main_menu = "1. Employees 2. Voyages 3. Destinations 4. Airplanes"
        #print("{}{}".format(true_menu, " " * (UIMain.TRUE_LEN - len(true_menu)-1)))
        print("-"*self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(main_menu, " "*(self.UI_DIVIDER_INT -
                                                len(main_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-"*self.UI_DIVIDER_INT)
        while True:
            choice = int(input("Input: "))
            nav_dict[choice]()


