from validation.validator import Validator
from models.Employee import Employee
models_validation = Validator()


class Pilot(Employee):
    def __init__(self, licence=''):
        super().__init__(self)
        self.__licence = licence

    def get_licence(self):
        return self.__licence

    def set_licence(self, new_licence):
        # if models_validation.validate_pilot_airplane_type:
        #     self.__airplane_type = new_airplane_type
        # else:
        #     pass
        self.__licence = new_licence
    def __str__(self):
        return super().__str__() + " " + self.__licence
