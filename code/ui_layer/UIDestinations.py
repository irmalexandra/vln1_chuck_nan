from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot

LENGTH = 52


class UIDestinations():
    def __init__(self):
        self.ll_api = LLAPI()

    def display_destination_sub_menu(self):
        print("-" * LENGTH)
        print("1. Create 2. All 3. Search")
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

    def display_all_destinations(self):
        print("-" * LENGTH)
        print("{:20}{:15}{:20}{:15}{:10}".format(
            "Country:", "Airport:", "Flight time:", "Distance:", "Contact name:", "Contact number:"))
        print("-" * LENGTH)
        destinations_list = self.ll_api.get_all_destinations_list()
        for destinations in destinations_list[1:]:
            print("{:20}{:15}{:20}{:15}{:10}".format(destinations.get_country(),
                                                     destinations.get_airport(),
                                                     destinations.get_flight_time(),
                                                     destinations.get_distance(),
                                                     destinations.get_contact_name(),
                                                     destinations.get_contact_number()))

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
