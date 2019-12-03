from logic_layer.LLAPI import LLAPI
from models import *

LENGTH = 52


class UIVoyages():
    def __init__(self):
        ll_api = LLAPI()

    def display_voyage_sub_menu(self):
        print("-" * LENGTH)
        print("1. Create 2. All 3. Search by 0. Home")
        print("-" * LENGTH)

    def display_voyage_search_menu(self):
        print("-" * LENGTH)
        print("1. Destination 2. Period 3. Empty Voyages 0. Home")
        print("-" * LENGTH)

    def display_voyage(self, voyage_id):
        print("Destination: ")

        print("Airplane: ")
        print("Departure date: ")
        print("Departure time: ")
        print("Return date: ")
        print("Return time: ")

        print("Departure flight number: ")
        print("Return flight number: ")

        print("Available seats: ")
        print("Sold seats: ")

        print("Status: ")

        print("Pilot: ")
        print("Co-Pilot: ")
        print("Flight Service Manager: ")
        print("Cabin Crew: ")
            Person1
            Person2
            Person3

    def display_all_voyages(self):
        print("Date           Country      Airport    Staffed")

    def display_all_empty_voyages(self):
        print("Index   Date           Country      Airport    Staffed")


    def display_all_voyages_by_period(self):
        period = input("Enter period (dd/mm/yyy-dd/mm/yyy): ")

    def display_all_voyages_by_destination(self):
        pass

    def create_voyage(self):
        destination = input("Destination: ")

        airplane = input("Airplane: ")
        departure_date = input("Departure date: ")
        departure_time = input("Departure time: ")
        return_date = input("Return date: ")
        return_time = input("Return time: ")

        departure_flight_number = input("Departure flight number: ")
        return_flight_number = input("Return flight number: ")

        available_seats = input("Available seats: ")

    def add_crew(self):
        pilot = input("Select pilot: ")
        co_pilot = input("Select Co-Pilot: ")
        flight_service_management = ("Select flight service manager: ")
            add_crew = ("Select flight attendant (input 1 when done): ")

    def duplicate_voyage(self):
        pass

    def repeat_voyage(self):
        pass
