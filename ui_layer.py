from logic_layer import LLAPI
from models import *

LENGHT = 52

class UIEmployees():
    def __init__(self):
        dl_api = LLAPI()

    def display_employee_sub_menu(self):
        print("-" * LENGHT)
        print("1. Create 2. All 3. Search by")
        print("-" * LENGHT)

    def display_employee_search_menu(self):
        print("-" * LENGHT)
        print("1. SSN 2. Title 3. Date 4. Airplane 0.Home")
        print("-" * LENGHT)

    def display_employee_by_ssn(self, ssn):
        pass
    
    def display_all_employees(self):
        pass

    def display_all_employees_by_date(self):
        pass

    def display_all_employees_by_title(self):
        pass

    def display_pilots_by_airplane_type_sorted(self):
        pass

    def display_pilots_by_airplane_type_filtered(self):
        pass

    def create_employee(self):
        pass

    def change_airplane_type(self):
        pass


class UIVoyages():
    def __init__(self):
        dl_api = LLAPI()


    def display_voyage_sub_menu(self):
        print("-" * LENGHT)
        print("1. Create 2. All 3. Search by 0. Home")
        print("-" * LENGHT)
    
    def display_voyage_search_menu(self):
        print("-" * LENGHT)
        print("1. Destination 2. Period 3. Empty Voyages 0. Home")
        print("-" * LENGHT)

    def display_voyage(self, voyage_id):
        pass

    def display_all_voyages(self):
        pass

    def display_all_empty_voyages(self):
        pass

    def display_all_voyages_by_period(self):
        pass

    def display_all_voyages_by_destination(self):
        pass

    def create_voyage(self):
        pass

    def add_crew(self):
        pass

    def duplicate_voyage(self):
        pass

    def repeat_voyage(self):
        pass



class UIDestinations():
    def __init__(self):
        dl_api = LLAPI()

    def display_destination_sub_menu(self):
        print("-" * LENGHT)
        print("1. Create 2. All 3. Search 0. Home")
        print("-" * LENGHT)

    def display_destination_search_menu(self):
        print("-" * LENGHT)
        print("1. Change contact 2. Change emergency number 0. Home")
        print("-" * LENGHT)

    def display_destination(self, destination_id):
        pass

    def display_destinations(self):
        pass

    def create_destination(self):
        pass

    def change_contact(self, destination_id):
        pass

    def change_emergency_number(self, destination_id):
        pass

class UIAirplanes():
    def __init__(self):
        dl_api = LLAPI()

    def display_airplanes_sub_menu(self):
        print("-" * LENGHT)
        print("{}{}".format("1. Create 2. Display all", "0. Home"))
        print("-" * LENGHT)

    def display_airplanes(self):
        pass

    def create_airplane(self):
        pass


class UIMain():
    def __init__(self):
        ui_employees = UIEmployees()
        ui_voyages = UIVoyages()
        ui_destinations = UIDestinations()
        ui_airplanes = UIAirplanes()

    def display_main_menu(self):
        print("-" * LENGHT)
        print("1. Employees 2. Voyages 3. Destinations 4. Airplanes")
        print("-" * LENGHT)

def main():
    test = UIMain()
    test.display_main_menu()

main()