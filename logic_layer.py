from data_layer import DLAPI
from models import *

class LLAPI:
    def __init__(self):
        ll_employees = LLEmployees()
        ll_voyages = LLVoyages()
        ll_destinations = LLDestinations()
        ll_airplanes = LLAirplanes()

class LLEmployees:
    def __init__(self):
        dl_api = DLAPI()

    def validate_employee(self):
        pass

    def get_employee(self, employee_ID):
        pass

    def get_all_employees(self):
        pass

    def filter_all_employees_by_date(self):
        pass

    def filter_all_employees_by_title(self):
        pass

    def filter_pilots_by_airplane_type(self):
        pass

    def sort_pilots_bu_airplane_type(self):
        pass

    def create_work_scedule(self):
        pass

class LLVoyages:
    def __init__(self):
        dl_api = DLAPI()

    def validate_voyage(self):
        pass

    def get_voyage(self, voyage_ID):
        pass

    def get_all_voyages(self):
        pass

    def filter_all_empty_voyages(self):
        pass

    def filter_all_voyages_by_period(self):
        pass

    def filter_all_voyages_by_destination(self):
        pass

    def duplicate_voyages(self):
        pass

    def repeat_voyage(self):
        pass

    def add_crew(self):
        pass
    
class LLDestinations:
    def __init__(self):
        dl_api = DLAPI()

    def validate_destination(self):
        pass

    def get_destination(self, estination_ID):
        pass

    def get_all_destinations(self):
        pass
    
class LLAirplanes:
    def __init__(self):
        dl_api = DLAPI()

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        pass
