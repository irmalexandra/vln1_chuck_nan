from logic_layer import LLAPI
from ui_layer.UIEmployees import UIEmployees
from ui_layer.UIVoyages import UIVoyages
from ui_layer.UIDestinations import UIDestinations
from ui_layer.UIAirplanes import UIAirplanes
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot
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
        ui_employees = UIEmployees()
        ui_voyages = UIVoyages()
        ui_destinations = UIDestinations()
        ui_airplanes = UIAirplanes()

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

        main_menu = "1. Employees 2. Voyages 3. Destinations 4. Airplanes"
        #print("{}{}".format(true_menu, " " * (UIMain.TRUE_LEN - len(true_menu)-1)))
        print("-"*self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(main_menu, " "*(self.UI_DIVIDER_INT -
                                                len(main_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-"*self.UI_DIVIDER_INT)
