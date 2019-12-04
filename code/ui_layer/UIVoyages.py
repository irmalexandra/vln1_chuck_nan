from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot

LENGTH = 90


class UIVoyages():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self):
        self.ll_api = LLAPI()

    def display_voyage_sub_menu(self):
        ''' Print the destination menu '''
        voyage_menu = "1. Create 2. All 3. Search"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(voyage_menu, " "*(self.UI_DIVIDER_INT - len(voyage_menu) -
                                                  len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-" * self.UI_DIVIDER_INT)

    def create_voyage(self):
        ''' Create a voyage '''
        # 1
        destination = input("Destination: ")
        airplane = input("Airplane: ")
        departure_date = input("Departure date: ")
        departure_time = input("Departure time: ")
        return_date = input("Return date: ")
        return_time = input("Return time: ")
        departure_flight_number = input("Departure flight number: ")
        return_flight_number = input("Return flight number: ")

    def display_all_voyages(self):
        ''' Print all voyages '''
        # 2
        print("-" * self.UI_DIVIDER_INT)
        print("{:15}{:11}{:27}{:27}{:27}{:27}{:17}".format(
            "Destination:", "Airplane:", "Departure date and time:", "Return date and time:", "Departure flight number:", "Return flight number:", "Status"))
        print("-" * self.UI_DIVIDER_INT)
        voyages_list = self.ll_api.get_all_voyages_list()
        for voyages in voyages_list[1:]:
            print("{:15}{:11}{:27}{:27}{:27}{:27}{:17}".format(voyages.get_return_flight_departing_from(),
                                                               voyages.get_aircraft_id(),
                                                               voyages.get_departing_flight_departure_date(),
                                                               voyages.get_return_flight_arrival_date(),
                                                               voyages.get_departing_flight_num(),
                                                               voyages.get_return_flight_num(),
                                                               "Missing status"))

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

        print("Person 1: ")
        print("Person 2: ")
        print("Person 3: ")

    # def display_all_voyages(self):
    #     print("Date           Country      Airport    Staffed")

    # def display_all_empty_voyages(self):
    #     print("Index   Date           Country      Airport    Staffed")

    def display_all_voyages_by_period(self):
        period = input("Enter period (dd/mm/yyy-dd/mm/yyy): ")

    def display_all_voyages_by_destination(self):
        pass

    def add_crew(self):
        pilot = input("Select pilot: ")
        co_pilot = input("Select Co-Pilot: ")
        flight_service_management = ("Select flight service manager: ")
        add_crew = ("Select flight attendant (input 1 when done): ")

    def duplicate_voyage(self):
        pass

    def repeat_voyage(self):
        pass
