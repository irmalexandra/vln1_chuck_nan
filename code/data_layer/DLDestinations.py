from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot

class DLDestinations():
    AIRPORT = 0
    COUNTRY = 1
    CITY = 2
    FLIGHT_TIME = 3
    DISTANCE = 4
    CONTACT_NAME = 5
    CONTACT_NUMBER = 6

    def __init__(self):
        self.all_destinations_list = []

    def pull_all_destinations(self):
        
        filestream = open("./repo/Destination.csv", "r")
        for line in filestream:
            line_list = line.strip().split(",")
            new_destination = Destination()

            new_destination.set_airport(line_list[DLDestinations.AIRPORT])
            new_destination.set_country(line_list[DLDestinations.COUNTRY])
            new_destination.set_city(line_list[DLDestinations.CITY])
            new_destination.set_flight_time(line_list[DLDestinations.FLIGHT_TIME])
            new_destination.set_distance(line_list[DLDestinations.DISTANCE])
            new_destination.set_contact_name(line_list[DLDestinations.CONTACT_NAME])
            new_destination.set_contact_num(line_list[DLDestinations.CONTACT_NUMBER])

            self.all_destinations_list.append(new_destination)
        filestream.closed
        return self.all_destinations_list[1:]

    def push_all_destinations(self):
        pass

