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

    def get_all_destinations_list(self):
        return self.ll_destinations.get_all_destinations()

    def get_all_airplanes_list(self):
        return self.ll_airplanes.get_all_airplanes()

    def get_all_voyages_list(self):
        return self.ll_voyages.get_all_voyages()

    def get_employee_list_by_title(self, title):
        return self.ll_employees.filter_all_employees_by_title(title)

    def get_employee_by_ssn(self, ssn):
        return self.ll_employees.get_employee_by_ssn(ssn)
