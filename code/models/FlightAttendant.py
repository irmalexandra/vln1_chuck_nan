from validation.validator import Validator
from models.Employee import Employee

models_validation = Validator()


class FlightAttendant(Employee):
    def __init__(self):
        super().__init__(self)
    
    def raw_info(self):
        print("-->",super().raw_info())
        return super().raw_info() + ",N/A\n"
