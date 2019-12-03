from models.Airplane import Airplane
from models.Employee import Employee
from models.Pilot import Pilot
from models.FlightAttendant import FlightAttendant
from models.Voyage import Voyage
from models.Destination import Destination



class ModelController():
    def __init__(self):
        self.model_dict = {"Airplane": Airplane,\
                      "Employee": Employee,\
                      "Pilot": Pilot,\
                      "FlightAttendant": FlightAttendant,\
                      "Voyage": Voyage,\
                      "Destination": Destination}

    def request_model(self, model_name):
        model_obj = self.model_dict[model_name]
        return model_obj()
