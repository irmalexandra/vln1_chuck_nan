from models import *


class DLAPI():
    def __init__(self):
        self.dl_employees = DLEmployees()
        self.dl_voyages = DLVoyages()
        self.dl_destinations = DLDestinations()
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

    def pull_all_employees():
        all_crew_list = []
        filestream = open("Crew.csv", "r")
        for line in filestream:
            all_crew_list.append(line.strip("\n").split(","))
        return all_crew_list[1:]

    def push_all_employees(self):
        pass


class DLVoyages():
    def __init__(self):
        pass

    def pull_all_voyages(self):
        all_voyages_list = []
        filestream = open("Flights.csv", "r")
        for line in filestream:
            all_voyages_list.append(line.strip("\n").split(","))
        return all_voyages_list[1:]

    def push_all_voyages(self):
        pass


class DLDestinations():
    def __init__(self):
        pass

    def pull_all_destinations(self):
        all_destinations_list = []
        filestream = open("Destinations.csv", "r")
        for line in filestream:
            all_destinations_list.append(line.strip("\n").split(","))
        return all_destinations_list[1:]

    def push_all_destinations(self):
        pass


class DLAirplanes():
    def __init__(self):
        pass

    def pull_all_airplanes(self):
        all_airplanes_list = []
        filestream = open("Aircraft.csv", "r")
        for line in filestream:
            all_airplanes_list.append(line.strip("\n").split(","))
        return all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass
