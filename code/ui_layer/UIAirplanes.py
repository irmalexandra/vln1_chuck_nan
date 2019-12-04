from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class UIAirplanes():
    UI_DIVIDER = 104

    def __init__(self):
        self.ll_api = LLAPI()

    def display_airplanes_sub_menu(self):
        print("-" * self.UI_DIVIDER)
        print("{}{}".format("1. Create 2. Display all", "0. Home"))
        print("-" * self.UI_DIVIDER)

    def display_airplanes(self):
        print("ID    Make    Model   TotalSeats  Status  Destination  Flight number  Date available  Time available")

    def create_airplane(self):
        name = input("ID: ")
        make = input("Make: ")
        model = input("Model: ")
        total_seats = input("Total seats: ")

    def display_all_airplanes(self):
        print("-" * self.UI_DIVIDER)
        print("{:12}{:12}{:12}{:12}".format(
            "ID:", "Make:", "Model:", "Total seats:"))
        print("-" * self.UI_DIVIDER)
        airplanes_list = self.ll_api.get_all_airplanes_list()
        for airplanes in airplanes_list[1:]:
            print("{:12}{:12}{:12}{:12}".format(airplanes.get_name(),
                                                airplanes.get_make(),
                                                airplanes.get_model(),
                                                airplanes.get_max_seats()))
