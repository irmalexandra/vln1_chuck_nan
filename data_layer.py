from models import *

class DLAPI():
    def __init__(self):
        self.dl_employees = DLEmployees()
        self.dl_voyages = DLVoyages()
        self.dl_airplanes = DLAirplanes()

    def populate_all_employees(self):
        self.all_employees_list = DLEmployees.pull_all_employees()
        pass

    def populate_all_voyages(self):
        self.all_voyages_list = DLVoyages.pull_all_voyages()
        pass

    def populate_all_destinations(self):
        self.all_destinations_list = DLDestinations.pull_all_destinations()
        pass

    def populate_all_airplanes(self):
        self.all_airplanes_list = DLAirplanes.pull_all_airplanes()
        pass


class DLEmployees():
    def __init__(self):
        pass

    def pull_all_employees(self):
        pass

    def push_all_employees(self):
        pass


class DLVoyages():
    def __init__(self):
        pass

    def pull_all_voyages(self):
        pass

    def push_all_voyages(self):
        pass


class DLDestinations():
    def __init__(self):
        pass

    def pull_all_destinations(self):
        pass

    def push_all_destinations(self):
        pass


class DLAirplanes():
    def __init__(self):
        pass

    def pull_all_airplanes(self):
        pass

    def push_all_airplanes(self):
        pass
