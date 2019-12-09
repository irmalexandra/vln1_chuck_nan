from data_layer.DLAPI import DLAPI
from logic_layer.LLEmployees import LLEmployees
from logic_layer.LLVoyages import LLVoyages
from logic_layer.LLDestinations import LLDestinations
from logic_layer.LLAirplanes import LLAirplanes
from models.ModelAPI import ModelAPI
from models.Employee import Employee


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

    def get_all_voyage_list_by_period_list(self, start_date, end_date):
        return self.__ll_voyages.filter_all_voyages_by_period(start_date, end_date)

    def get_all_voyage_list_by_airport(self, airport):
        return self.__ll_voyages.filter_all_voyages_by_airport(airport)

    def get_filtered_employee_list_for_voyage(self, rank, voyage):
        return self.__ll_voyages.filter_available_employees(rank, voyage)

    def get_employee_list_by_title(self, title):
        return self.__ll_employees.filter_all_employees_by_title(title)

    def get_destination_list_by_country(self, country):
        return self.__ll_destinations.get_destination_list_by_country(country)

    def edit_destination(self, destination, input_tpl):
        return self.__ll_destinations.edit_destination(destination, input_tpl)

    def get_airplane_type_list(self):
        return self.__ll_airplanes.get_airplane_type_list()
        
    def get_all_available_airplane_list(self, voyage):
        return self.__ll_airplanes.filter_available_airplanes(voyage)

    def create_airplane(self, airplane, airplane_types, insignia):
        return self.__ll_airplanes.create_airplane(airplane, airplane_types, insignia)
        
    def get_employee_list_filtered_by_name(self, search_string):
        return self.__ll_employees.filter_employees_by_name(search_string)
   
    def get_pilot_list_sorted_by_airplane_type(self):
        return self.__ll_employees.sort_pilots_by_airplane_type()
    
    def get_pilot_list_filtered_by_airplane_type(self, airplane_type):
        return self.__ll_employees.filter_pilots_by_airplane_type(airplane_type)

    def get_work_schedule_list(self, employee):
        return self.__ll_employees.get_work_schedule_list(employee)

    def overwrite_all_models(self,model):
        check = self.__modelAPI.validate_edit_model(model)
        if type(check).__name__ != "str":
            if type(model).__name__ == "Employee":
                return self.__ll_employees.overwrite_all_employees()
            if type(model).__name__ == "Airplane":
                return self.__ll_airplanes.overwrite_all_employees()
            if type(model).__name__ == "Destination":
                return self.__ll_destinations.overwrite_all_destinations()
            if type(model).__name__ == "Voyage":
                return self.__ll_voyages.overwrite_all_voyages()
        else:
            return check

    def add_crew_member_to_voyage(self):
        return 


    def duplicate_voyage(self, voyage, new_date):
        return self.__ll_voyages.duplicate_voyage(voyage, new_date)