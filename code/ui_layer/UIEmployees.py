from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


LENGTH = 52


class UIEmployees():
    def __init__(self):
        ll_api = LLAPI()

    def display_employee_sub_menu(self):
        print("-" * LENGTH)
        print("1. Create 2. All 3. Search by")
        print("-" * LENGTH)

    def display_employee_search_menu(self):
        print("-" * LENGTH)
        print("1. SSN 2. Title 3. Date 4. Airplane 0.Home")
        print("-" * LENGTH)

    def display_employee_by_ssn(self, ssn):
        pass

    def display_all_employees(self):
        print("Name    SSN    Title   License    Availability")

    def display_all_employees_by_date(self):
        print()
        pass

    def display_all_employees_by_title(self):
        pass

    def display_pilots_by_airplane_type_sorted(self):
        pass

    def display_pilots_by_airplane_type_filtered(self):
        pass

    def create_employee(self):
        name = input("Name: ")
        SSN = input("SSN: ")
        home_number = input("Home number: ")
        mobile_number = input("Mobile number: ")
        email = input("E-mail: ")
        title = input("Title: ")
        licence = input("Licence: ")
        availability = input("Availability: ")

    def change_airplane_type(self):
        pass
