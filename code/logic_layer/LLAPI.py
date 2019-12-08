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
        return self.__ll_employees.get_all_employee_list()

    def get_employee_list_by_name(self):
        return self.__ll_employees.sort_all_employees_by_name()

    def get_all_destination_list(self):
        return self.__ll_destinations.get_all_destination_list()

    def get_all_airplane_list(self):
        return self.__ll_airplanes.get_all_airplane_list()

    def get_all_voyage_list(self):
        return self.__ll_voyages.get_all_voyage_list()

    def get_all_empty_voyage_list(self):
        return self.__ll_voyages.filter_all_empty_voyages()

    def get_employee_list_by_title(self, title):
        return self.__ll_employees.filter_all_employees_by_title(title)

    def get_destination_list_by_country(self, country):
        return self.__ll_destinations.get_destination_list_by_country(country)

    def edit_destination(self, destination, input_tpl):
        return self.__ll_destinations.edit_destination(destination, input_tpl)

    def get_airplane_type_list(self):
        return self.__ll_airplanes.get_airplane_type_list()

    def create_airplane(self, airplane, airplane_types, insignia):
        return self.__ll_airplanes.create_airplane(airplane, airplane_types, insignia)
        
    def get_employee_list_filtered_by_name(self, search_string):
        return self.__ll_employees.filter_employees_by_name(search_string)

    def clear_airplane_lists(self):
        self.__DLAPI.clear_airplane_lists()
        
    def get_pilot_list_sorted_by_airplane_type(self):
        return self.__ll_employees.sort_pilots_by_airplane_type()
    
    def get_pilot_list_filtered_by_airplane_type(self, airplane_type):
        return self.__ll_employees.filter_pilots_by_airplane_type(airplane_type)

    def get_work_schedule_list(self, employee):
        return self.__ll_employees.get_work_schedule_list(employee)

