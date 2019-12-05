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

    def get_all_employee_list(self):
        return self.__ll_employees.get_all_employees()

    def get_employee_list_by_name(self):
        return self.__ll_employees.list_all_employees_by_name()

    def get_all_destinations_list(self):
        return self.__ll_destinations.get_all_destinations()

    def get_all_airplanes_list(self):
        return self.__ll_airplanes.get_all_airplanes()

    def get_all_voyages_list(self):
        return self.__ll_voyages.get_all_voyages()

    def get_employee_list_by_title(self, title):
        return self.__ll_employees.filter_all_employees_by_title(title)

    def get_employee_by_name(self, search_string):
        return self.__ll_employees.get_employee_by_name(name)

    def get_one_destination(self, airport):
        return self.__ll_destinations.get_one_destination(airport)

    def edit_destination(self, input_tpl):
        return self.__ll_destinations.edit_destination(input_tpl)

    def create_airplane(self, airplane):
        return self.__ll_airplanes.create_airplane(airplane)

    def get_employees_filtered_by_name(self, name):
        return self.__ll_employees.get_employees_by_name(name)
