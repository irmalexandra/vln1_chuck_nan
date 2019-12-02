from models import *

class DLAPI():
    def __init__(self):
        self.dl_employees = DLEmployees()
        self.dl_voyages = DLVoyages()
        self.dl_destinations = DLDestinations()
        self.dl_airplanes = DLAirplanes()

    def populate_all_employees(self):
        return self.dl_employees.pull_all_employees()

    def populate_all_voyages(self):
        return self.dl_voyages.pull_all_voyages()

    def populate_all_destinations(self):
        return self.dl_destinations.pull_all_destinations()

    def populate_all_airplanes(self):
        return self.dl_airplanes.pull_all_airplanes()

class DLEmployees():
    def __init__(self):
        pass
    def pull_all_employees(self):
        all_crew_list = []
        filestream = open("Crew.csv","r")
        for line in filestream:
            all_crew_list.append(line.strip("\n").split(","))
        filestream.closed
        return all_crew_list[1:]

    def push_all_employees(self):
        pass

class DLVoyages():
    def __init__(self):
        pass

    def pull_all_voyages(self):
        all_voyages_list = []
        filestream = open("Flight.csv", "r")
        for line in filestream:
            all_voyages_list.append(line.strip("\n").split(","))
        filestream.closed
        return all_voyages_list[1:]

    def push_all_voyages(self):
        pass


class DLDestinations():
    def __init__(self):
        pass

    def pull_all_destinations(self):
        all_destinations_list = []
        filestream = open("Destination.csv", "r")
        for line in filestream:
            all_destinations_list.append(line.strip("\n").split(","))
        filestream.closed
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
        filestream.closed
        return all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass


stuff = DLAPI()
print("What", stuff.populate_all_employees())
print("\n", stuff.populate_all_airplanes())
print("\n", stuff.populate_all_destinations())
print("\n", stuff.populate_all_voyages())
