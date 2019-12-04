from data_layer.DLAirplanes import DLAirplanes
from data_layer.DLDestinations import DLDestinations
from data_layer.DlEmployees import DLEmployees
from data_layer.DLVoyages import DLVoyages
from models.ModelController import ModelController


class DLAPI():
    def __init__(self):
        self.__model_controller = ModelController()
        self.__dl_employees = DLEmployees(self.__model_controller)
        self.__dl_voyages = DLVoyages(self.__model_controller)
        self.__dl_destinations = DLDestinations(self.__model_controller)
        self.__dl_airplanes = DLAirplanes(self.__model_controller)

    def populate_all_employees(self):
        return self.__dl_employees.pull_all_employees()

    def populate_all_voyages(self):
        return self.__dl_voyages.pull_all_voyages()

    def populate_all_destinations(self):
        return self.__dl_destinations.pull_all_destinations()

    def populate_all_airplanes(self):
        return self.__dl_airplanes.pull_all_airplanes()
