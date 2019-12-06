from data_layer.DLAirplanes import DLAirplanes
from data_layer.DLDestinations import DLDestinations
from data_layer.DlEmployees import DLEmployees
from data_layer.DLVoyages import DLVoyages
from models.ModelAPI import ModelAPI


class DLAPI():
    def __init__(self):
        self.__modelAPI = ModelAPI()
        self.__dl_employees = DLEmployees(self.__modelAPI)
        self.__dl_voyages = DLVoyages(self.__modelAPI)
        self.__dl_destinations = DLDestinations(self.__modelAPI)
        self.__dl_airplanes = DLAirplanes(self.__modelAPI)

    def pull_all_employees(self):
        '''Get a list of all employees from data layer and returns it'''
        return self.__dl_employees.pull_all_employees()

    def overwrite_all_employees(self, employee_list):
        self.__dl_employees.push_all_employees(employee_list)

    def pull_all_voyages(self):
        '''Gets a list of all voyages from the data layer and returns it'''
        return self.__dl_voyages.pull_all_voyages()

    def pull_all_destinations(self):
        '''Gets a list of all destinations from the data layer and returns it'''
        return self.__dl_destinations.pull_all_destinations()

    def overwrite_all_destinations(self, destination_list):
        self.__dl_destinations.push_all_destinations(destination_list)
        
    def pull_all_airplanes(self):
        '''Gets a list of all airplanes from the data layer and returns it'''
        return self.__dl_airplanes.pull_all_airplanes()
    
    def pull_all_airplane_types(self):
        '''Gets a list of all airplane types from the data layer and returns it'''
        return self.__dl_airplanes.pull_airplane_types_info()
    
    def create_airplane(self, airplane):
        self.__dl_airplanes.append_airplane(airplane)
