from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot

class DLVoyages():
    DEPARTING_FLIGHT_NUM = 0
    RETURNING_FLIGHT_NUM = 1
    DEPARTING_FLIGHT_DEPARTING_FROM = 2
    DEPARTING_FLIGHT_DEPARTING_DATE = 3
    DEPARTING_FLIGHT_ARRIVAL_DATE = 4
    RETURNING_FLIGHT_DEPARTING_FROM = 5
    RETURNING_FLIGHT_DEPARTURE_DATE = 6
    RETURNING_FLIGHT_ARRIVAL_DATE= 7
    AIRCRAFT_ID = 8
    CAPTAIN_ID = 9
    COPILOT_ID = 10
    FSMID = 11
    FAIDS = 12

    def __init__(self):
        self.all_voyages_list = []

    def pull_all_voyages(self):
        
        filestream = open("./repo/Flight.csv", "r")
        for line in filestream:
            self.all_voyages_list.append(line.strip("\n").split(","))
        filestream.closed
        return self.all_voyages_list

    def push_all_voyages(self):
        pass
