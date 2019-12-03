from data_layer.DLAPI import DLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class LLEmployees:
    def __init__(self):
        self.dl_api = DLAPI()

    def validate_employee(self):
        pass

    def get_employee(self, employee_ID):
        pass

    def get_all_employees(self):
        return self.dl_api.populate_all_employees()

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
