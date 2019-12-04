from data_layer.DLAPI import DLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class LLVoyages:
    def __init__(self):
        self.dl_api = DLAPI()

    def validate_voyage(self):
        pass

    def get_voyage(self, voyage_ID):
        pass

    def get_all_voyages(self):
        return self.dl_api.populate_all_voyages()

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
