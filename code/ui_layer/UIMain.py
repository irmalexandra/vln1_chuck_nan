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
LENGTH = 90


class UIMain():
    LINE_LEN = 88
    T_LEN = 8
    TRUE_LEN = LINE_LEN + 2 * T_LEN
    distinguisher = "{}\n{}\n\n".format("_"*TRUE_LEN,"_"*TRUE_LEN)

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
        print(UIMain.distinguisher,end="")

    def display_main_menu(self):
        
        true_menu = "1. Employees 2. Voyages 3. Destinations 4. Airplanes"
        true_menu2 = "1.  kakk"
        true_menu3 = "1.  Idk fam  2.  help"
        print("|{}{}|".format(true_menu," " * (UIMain.TRUE_LEN - len(true_menu)-1)))
        print("|{}{}|".format(true_menu2," " * (UIMain.TRUE_LEN - len(true_menu2)-1)))
        print("|{}{}|".format(true_menu3," " * (UIMain.TRUE_LEN - len(true_menu3)-1)))
        #print("-" * LENGTH)
        #print("1. Employees 2. Voyages 3. Destinations 4. Airplanes")
        #print("-" * LENGTH)
