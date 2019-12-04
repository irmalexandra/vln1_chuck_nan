from models.ModelController import ModelController


class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    AIRCRAFT_DICT_PLANE_TYPE = 0
    AIRCRAFT_DICT_MODEL = 1
    AIRCRAFT_DICT_CAPACITY = 2

    def __init__(self):
        self.all_airplanes_list = []
        self.__model_controller = ModelController()

    def pull_all_airplanes(self):

        aircraft_stream = open("./repo/Aircraft.csv", "r")
        type_stream = open("./repo/AircraftType.csv", "r")

        type_stream_list = [line.strip().split(",") for line in type_stream]
        type_dict = dict()
        for aircraft_info in type_stream_list:
            type_dict[aircraft_info[DLAirplanes.PLANE_TYPE_ID]] = aircraft_info[1:]

        for line in aircraft_stream:
            line_list = line.strip().split(",")
            new_aircraft = self.__model_controller.get_model('Airplane')
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

    def append_aircraft(self, aircraft):
        aircraft_stream = open('./repo/Aircraft.csv', 'a')
        aircraft_str = aircraft.raw_info()
        aircraft_stream.write(aircraft_str)
        aircraft_stream.close()
        return    
