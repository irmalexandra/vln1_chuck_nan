from logic_layer.LLAPI import LLAPI


LENGTH = 52


class UIAirplanes():
    def __init__(self):
        ll_api = LLAPI()

    def display_airplanes_sub_menu(self):
        print("-" * LENGTH)
        print("{}{}".format("1. Create 2. Display all", "0. Home"))
        print("-" * LENGTH)

    def display_airplanes(self):
        print("Name    Make    Model   TotalSeats  Status  Destination  Flight number  Date available  Time available")

    def create_airplane(self):
        name = input("Name: ")
        make = input("Make: ")
        model = input("Model: ")
        total_seats = input("Total seats: ")
