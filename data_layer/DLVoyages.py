from models import *

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
