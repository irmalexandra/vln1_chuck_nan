from logic_layer import LLAPI
from models import *

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
