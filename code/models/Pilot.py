from validation.validator import Validator
from models.Employee import Employee
class Pilot(Employee):
    def __init__(self, licence=''):
        super().__init__(self)
        self.__licence = licence
        self.__header_format_dict = {"default": self.get_model_header_aircraft_format}
        self.__list_info_dict = {"default": self.get_model_list_aircraft_info }

    def get_licence(self):
        return self.__licence

    def set_licence(self, new_licence):
        # if self.__models_validation.validate_pilot_airplane_type:
        #     self.__airplane_type = new_airplane_type
        # else:
        #     pass
        self.__licence = new_licence
    def __str__(self):
        return super().__str__() + " licence: " + self.__licence

    def raw_info(self):
        return super().raw_info() + "," + self.__licence + "\n"

    