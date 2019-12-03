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

LENGTH = 52


class UIMain():
    def __init__(self):
        ui_employees = UIEmployees()
        ui_voyages = UIVoyages()
        ui_destinations = UIDestinations()
        ui_airplanes = UIAirplanes()

    def display_main_menu(self):
        print("-" * LENGTH)
        print("1. Employees 2. Voyages 3. Destinations 4. Airplanes")
        print("-" * LENGTH)


def main():
    test = UIMain()
    test.display_main_menu()


main()
