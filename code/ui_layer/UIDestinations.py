from logic_layer.LLAPI import LLAPI
from models import *

LENGTH = 52


class UIDestinations():
    def __init__(self):
        ll_api = LLAPI()

    def display_destination_sub_menu(self):
        print("-" * LENGTH)
        print("1. Create 2. All 3. Search 0. Home")
        print("-" * LENGTH)

    def display_destination_search_menu(self):
        print("-" * LENGTH)
        print("1. Change contact 2. Change emergency number 0. Home")
        print("-" * LENGTH)

    def display_destination(self, destination_id):
        print("Country: ")
        print("Airport: ")
        print("Flight time: ")
        print("Distance: ")
        print("Contact name: ")
        print("Contact number: ")

    def display_destinations(self):
        print("Country     Airport     Distance    FlightTime      ContactName     ContactNumber")

    def create_destination(self):
        country = input("Country: ")
        airport = input("Airport: ")
        flight_time = input("Flight time: ")
        distance = input("Distance: ")
        contact_name = input("Contact name: ")
        contact_number = input("Contact number: ")

    def change_contact(self, destination_id):
        pass

    def change_emergency_number(self, destination_id):
        pass
