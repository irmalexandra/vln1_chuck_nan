from models import *

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

