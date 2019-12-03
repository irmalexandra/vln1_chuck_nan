from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot

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

