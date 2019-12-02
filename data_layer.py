from models import *

def open_file(file_name):
    """ Opens a file, returns Error if wrong, else returns file as object file"""
    try:
        file_object = open(file_name, "r")
    except FileNotFoundError:
        print("File " + str(file_name) + " not found!")
        return None
    return file_object

def read_file(a_file):
    returned_list = []
    for line in a_file:
        line_list = line.strip().split()
        returned_list.append(line_list)

    return returned_list
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

    def pull_all_employees(self):
        file_name = "Crew.csv"
        file_object = open_file(file_name)

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
