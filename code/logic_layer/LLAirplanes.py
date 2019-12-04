from data_layer.DLAPI import DLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class LLAirplanes:
    def __init__(self):
        self.dl_api = DLAPI()

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.dl_api.populate_all_airplanes()
