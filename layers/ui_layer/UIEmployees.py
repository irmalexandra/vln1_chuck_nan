from logic_layer import LLAPI
from models import *

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
