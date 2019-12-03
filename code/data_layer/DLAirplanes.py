from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    AIRCRAFT_DICT_PLANE_TYPE = 1
    AIRCRAFT_DICT_MODEL = 2
    AIRCRAFT_DICT_CAPACITY = 3

    def __init__(self):
        self.all_airplanes_list = []

    def pull_all_airplanes(self):

        aircraft_stream = open("./repo/Aircraft.csv", "r")
        type_stream = open("./repo/AircraftType.csv", "r")

        type_stream_list = [line.strip().split(",") for line in type_stream]
        type_dict = dict()
        for aircraft_info in type_stream_list:
            type_dict[aircraft_info[DLAirplanes.PLANE_TYPE_ID]] = aircraft_info[1:]

        for line in aircraft_stream:
            line_list = line.strip().split(",")
            new_aircraft = Airplane()
            plane_type = line_list[DLAirplanes.PLANE_TYPE_ID]
            new_aircraft.set_name(line_list[DLAirplanes.PLANE_NAME]) #Insignia
            aircraft_info_list = type_dict[plane_type]
            new_aircraft.set_make(aircraft_info_list[DLAirplanes.AIRCRAFT_DICT_PLANE_TYPE])   #planeType
            new_aircraft.set_model(aircraft_info_list[DLAirplanes.AIRCRAFT_DICT_MODEL])    #Model
            new_aircraft.set_max_seats(aircraft_info_list[DLAirplanes.AIRCRAFT_DICT_CAPACITY])    #Capacity




            self.all_airplanes_list.append(new_aircraft)
        aircraft_stream.close()
        type_stream.close()
        return self.all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass
