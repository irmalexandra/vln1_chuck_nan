from validation.validator import Validator
from models.Employee import Employee
class FlightAttendant(Employee):
    def __init__(self):
        super().__init__(self)
    
    def raw_info(self):
        return super().raw_info() + ",N/A\n"
