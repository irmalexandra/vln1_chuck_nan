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

    def populate_all_employees(self):
        return self.__dl_employees.pull_all_employees()

    def populate_all_voyages(self):
        return self.__dl_voyages.pull_all_voyages()

    def populate_all_destinations(self):
        return self.__dl_destinations.pull_all_destinations()

    def populate_all_airplanes(self):
        return self.__dl_airplanes.pull_all_airplanes()
    
    def populate_all_airplane_types(self):
        return self.__dl_airplanes.pull_airplane_types_info()
    
    def create_airplane(self, airplane):
        self.__dl_airplanes.append_aircraft(airplane)
