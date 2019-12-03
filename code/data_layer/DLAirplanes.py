from models.Airplane import Airplane

class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    PLANE_MAKE = 1
    PLANE_MODEL = 2
    MAX_SEATS = 3
    def __init__(self):
        self.all_airplanes_list = []

    def pull_all_airplanes(self):
        
        aircraft_stream = open("./repo/Aircraft.csv", "r")
        type_stream = open("./repo/AircraftType.csv", "r")

        type_stream_list = [line.strip().split(",") for line in type_stream]
        type_dict = dict()
        for aircraft_info in type_stream_list[1:]:
            type_dict[aircraft_info[DLAirplanes.PLANE_TYPE_ID]] = aircraft_info[1:]
        for item in type_dict.items():
            print(item)
        for line in aircraft_stream:
            line_list = line.strip().split(",")
            new_aircraft = Airplane()

            new_aircraft.set_name(line_list[DLAirplanes.PLANE_NAME])




            self.all_airplanes_list.append(line.strip("\n").split(","))
        aircraft_stream.close()
        type_stream.close()
        return self.all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass

