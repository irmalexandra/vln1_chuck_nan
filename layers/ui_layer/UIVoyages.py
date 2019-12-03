from logic_layer import LLAPI
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
