from validation.validator import Validator
from models.Employee import Employee

models_validation = Validator()


class FlightAttendant(Employee):
    def __init__(self):
        super().__init__(self)
