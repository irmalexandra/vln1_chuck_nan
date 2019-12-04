from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class UIDestinations():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self):
        self.ll_api = LLAPI()

    def display_destination_sub_menu(self):
        ''' Print the destination menu '''
        destination_menu = "1. Create 2. All 3. Search"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(destination_menu, " "*(self.UI_DIVIDER_INT - len(destination_menu) -
                                                       len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-" * self.UI_DIVIDER_INT)

    def create_destination(self):
        ''' Create a destination '''
        # 1
        # user input
        country = input("Country: ")
        airport = input("Airport: ")
        flight_time = input("Flight time: ")
        distance = input("Distance: ")
        contact_name = input("Contact name: ")
        contact_number = input("Contact number: ")

    def display_create_destination_header(self):
        counter = 1
        header = "Create Destination " 
        print ("{}{}".format(header, "("+ counter + "/6)"))
    
    def display_all_destinations(self):
        ''' Print all destinations '''
        # 2
        print("-" * self.UI_DIVIDER_INT)
        print("{:19}{:15}{:17}{:15}{:20}{:10}".format(
            "Country:", "Airport:", "Flight time:", "Distance:", "Contact name:", "Contact number:"))
        print("-" * self.UI_DIVIDER_INT)
        destinations_list = self.ll_api.get_all_destinations_list()
        for destinations in destinations_list[1:]:
            print("{:19}{:15}{:17}{:15}{:20}{:10}".format(destinations.get_country(),
                                                          destinations.get_airport(),
                                                          destinations.get_flight_time(),
                                                          destinations.get_distance(),
                                                          destinations.get_contact_name(),
                                                          destinations.get_contact_number()))

    def display_one_destination(self):
        ''' Search for a destination and print the information '''
        # 3
        # user input
        print("Country: ")
        print("Airport: ")
        print("Flight time: ")
        print("Distance: ")
        print("Contact name: ")
        print("Contact number: ")
        self.display_destination_search_menu()

    def display_destination_search_menu(self):
        ''' Change contact name or emergency number and print the information '''
        search_menu = "1. Change contact name 2. Change emergency number"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(search_menu, " "*(self.UI_DIVIDER_INT -
                                                  len(search_menu)-len(self.RETURN_MENU_STR)-self.DEVIATION_INT), self.RETURN_MENU_STR))
        print("-" * self.UI_DIVIDER_INT)

    def change_contact(self, destination_id):
        pass

    def change_emergency_number(self, destination_id):
        pass
