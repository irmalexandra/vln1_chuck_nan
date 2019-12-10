import os
from os import path

class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_INSIGNIA = 1
    AIRPLANE_DICT_PLANE_TYPE = 0
    AIRPLANE_DICT_MODEL = 1
    AIRPLANE_DICT_CAPACITY = 2
    PLANE_TYPE_ID = 0
    PLANE_TYPE_MAKE = 1
    PLANE_TYPE_MODEL = 2
    PLANE_TYPE_CAPACITY = 3
    CSV_ROWS = 2
    def __init__(self, modelAPI):
        
        self.__modelAPI = modelAPI




    def pull_all_airplanes(self):
        '''Opens csv files and returns a list of all the airplanes (type ID, insignia, type)'''
        airplane_stream = open("./repo/Airplane.csv", "r")
        type_stream = open("./repo/AirplaneType.csv", "r")
        all_airplanes_list = []
        type_stream_list = [line.strip().split(",") for line in type_stream]
        type_dict = dict()
        for airplane_info in type_stream_list:
            type_dict[airplane_info[DLAirplanes.PLANE_TYPE_ID]] = airplane_info[1:]

        for line in airplane_stream:
            line_list = line.strip().split(",")
            if len(line_list) == self.CSV_ROWS:
                new_airplane = self.__modelAPI.get_model('Airplane')
                plane_type = line_list[DLAirplanes.PLANE_TYPE_ID]
                new_airplane.set_insignia(line_list[DLAirplanes.PLANE_INSIGNIA])
                airplane_info_list = type_dict[plane_type]
                new_airplane.set_make(airplane_info_list[self.AIRPLANE_DICT_PLANE_TYPE])   #planeType
                new_airplane.set_model(airplane_info_list[self.AIRPLANE_DICT_MODEL])    #Model
                new_airplane.set_capacity(airplane_info_list[self.AIRPLANE_DICT_CAPACITY])    #Capacity

                all_airplanes_list.append(new_airplane)
        airplane_stream.close()
        type_stream.close()
        return all_airplanes_list[1:]
        
    def append_airplane(self, airplane):
        '''Adds a new airplane to the airplane string'''
        airplane_stream = open('./repo/Airplane.csv', 'a')
        airplane_str = airplane.raw_info()
        airplane_stream.write(airplane_str)
        airplane_stream.close()
        return    

    def pull_airplane_types_info(self):
        # Ath!!
        filestream = open("./repo/AirplaneType.csv", "r")
        new_airplane_type_list = []
        
        for airplane in filestream:
            check_list = []
            new_airplane_type = self.__modelAPI.get_model("AirplaneType")
            airplanes_types_list = airplane.strip().split(",")
            check_list.append(new_airplane_type.set_plane_type_id(airplanes_types_list[self.PLANE_TYPE_ID]))
            check_list.append(new_airplane_type.set_make(airplanes_types_list[self.PLANE_TYPE_MAKE]))
            check_list.append(new_airplane_type.set_model(airplanes_types_list[self.PLANE_TYPE_MODEL]))
            check_list.append(new_airplane_type.set_capacity(airplanes_types_list[self.PLANE_TYPE_CAPACITY]))      
            if False not in check_list:
                new_airplane_type_list.append(new_airplane_type)
        filestream.close()
        return new_airplane_type_list

    def overwrite_all_airplanes(self, airplane_list):

        HEADER = "planeTypeId,planeInsignia\n"
        filestream = open("./repo/Airplane_temp.csv", "w")
        filestream.write(HEADER)
        for airplane_info in airplane_list:
            filestream.write(airplane_info.raw_info())
        filestream.close()
        os.remove("./repo/Airplane.csv")
        os.rename("./repo/Airplane_temp.csv", "./repo/Airplane.csv")
        return 