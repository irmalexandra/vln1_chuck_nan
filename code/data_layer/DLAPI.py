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
        '''Gets a list of all employees from data layer and returns it'''
        return self.__dl_employees.pull_all_employees()

    def overwrite_all_employees(self, employee_list):
        return self.__dl_employees.overwrite_all_employees(employee_list)

    def append_employee(self, employee):
        return self.__dl_employees.append_employee(employee)

    def pull_all_voyages(self):
        '''Gets a list of all voyages from the data layer and returns it'''
        return self.__dl_voyages.pull_all_voyages()

    def overwrite_all_voyages(self, voyage_list):
        return self.__dl_voyages.overwrite_all_voyages(voyage_list)

    def append_voyage(self, voyage):
        return self.__dl_voyages.append_voyage(voyage)

    def pull_all_destinations(self):
        '''Gets a list of all destinations from the data layer and returns it'''
        return self.__dl_destinations.pull_all_destinations()

    def overwrite_all_destinations(self, all_destination_list):
        return self.__dl_destinations.overwrite_all_destinations(all_destination_list)
    
    def append_destination(self, destination):
        '''Adds a new destination to the list of destinations'''
        return self.__dl_destinations.append_destination(destination)

    def pull_all_airplanes(self):
        '''Gets a list of all airplanes from the data layer and returns it'''
        return self.__dl_airplanes.pull_all_airplanes()

    def overwrite_all_airplanes(self, airplane_list):
        return self.__dl_airplanes.overwrite_all_airplanes(airplane_list)

    def pull_all_airplane_types(self):
        '''Gets a list of all airplane types from the data layer and returns it'''
        return self.__dl_airplanes.pull_airplane_types_info()

    def append_airplane(self, airplane):
        return self.__dl_airplanes.append_airplane(airplane)
