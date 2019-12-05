from data_layer.DLAPI import DLAPI
from logic_layer.LLEmployees import LLEmployees
from logic_layer.LLVoyages import LLVoyages
from logic_layer.LLDestinations import LLDestinations
from logic_layer.LLAirplanes import LLAirplanes
from models.ModelAPI import ModelAPI


class LLAPI:
    def __init__(self):
        self.__DLAPI = DLAPI()
        self.__modelAPI = ModelAPI()
        self.__ll_employees = LLEmployees(self.__DLAPI, self.__modelAPI)
        self.__ll_voyages = LLVoyages(self.__DLAPI, self.__modelAPI)
        self.__ll_destinations = LLDestinations(self.__DLAPI, self.__modelAPI)
        self.__ll_airplanes = LLAirplanes(self.__DLAPI, self.__modelAPI)

    def get_all_employee_dict(self):
        return self.__ll_employees.get_all_employees()

    def get_all_destinations_dict(self):
        return self.__ll_destinations.get_all_destinations()

    def get_all_airplanes_dict(self):
        return self.__ll_airplanes.get_all_airplanes()

    def get_all_voyages_dict(self):
        return self.__ll_voyages.get_all_voyages()

    def get_employee_dict_by_title(self, title):
        return self.__ll_employees.filter_all_employees_by_title(title)

    def get_employee_by_ssn(self, ssn):
        return self.__ll_employees.get_employee_by_ssn(ssn)
