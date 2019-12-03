from logic_layer.LLEmployees import LLEmployees
from logic_layer.LLVoyages import LLVoyages
from logic_layer.LLDestinations import LLDestinations
from logic_layer.LLAirplanes import LLAirplanes
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class LLAPI:
    def __init__(self):
        self.ll_employees = LLEmployees()
        self.ll_voyages = LLVoyages()
        self.ll_destinations = LLDestinations()
        self.ll_airplanes = LLAirplanes()

    def get_all_employee_list(self):
        return self.ll_employees.get_all_employees()
