import os
from os import path

class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    AIRPLANE_DICT_PLANE_TYPE = 0
    AIRPLANE_DICT_MODEL = 1
    AIRPLANE_DICT_CAPACITY = 2
    PLANE_TYPE_ID = 0
    PLANE_TYPE_MAKE = 1
    PLANE_TYPE_MODEL = 2
    PLANE_TYPE_CAPACITY = 3
    def __init__(self, modelAPI):
        self.all_airplanes_list = []
        self.__modelAPI = modelAPI
        self.airplanes_types_list = []

    def clear_airplane_lists(self):
        self.all_airplanes_list.clear()
        self.airplanes_types_list.clear()


    def pull_all_airplanes(self):
        '''Opens csv files and returns a list of all the airplanes (type ID, name, type)'''

        if path.exists('./repo/Airplane.csv') and path.exists('./repo/Airplane_temp.csv'):
            airplane_stream = open("./repo/Airplane.csv", "r")
            os.remove("./repo/Airplane_temp.csv")
        elif path.exists('./repo/Airplane.csv') and path.exists('./repo/Airplane_temp.csv') == False:
            airplane_stream = open("./repo/Airplane.csv", "r")
        elif path.exists('./repo/Airplane.csv') == False and path.exists('./repo/Airplane_temp.csv'):
            airplane_stream = open("./repo/Airplane_temp.csv", "r")
        else:
            print("Airplane data files not found")
            return

        type_stream = open("./repo/AirplaneType.csv", "r")

        type_stream_list = [line.strip().split(",") for line in type_stream]
        type_dict = dict()
        for airplane_info in type_stream_list:
            type_dict[airplane_info[DLAirplanes.PLANE_TYPE_ID]] = airplane_info[1:]

        for line in airplane_stream:
            line_list = line.strip().split(",")
            new_airplane = self.__modelAPI.get_model('Airplane')
            plane_type = line_list[DLAirplanes.PLANE_TYPE_ID]
            new_airplane.set_name(line_list[DLAirplanes.PLANE_NAME]) #Insignia
            airplane_info_list = type_dict[plane_type]
            new_airplane.set_make(airplane_info_list[self.AIRPLANE_DICT_PLANE_TYPE])   #planeType
            new_airplane.set_model(airplane_info_list[self.AIRPLANE_DICT_MODEL])    #Model
            new_airplane.set_max_seats(airplane_info_list[self.AIRPLANE_DICT_CAPACITY])    #Capacity

            self.all_airplanes_list.append(new_airplane)
        airplane_stream.close()
        type_stream.close()
        return self.all_airplanes_list[1:]
        
    def append_airplane(self, airplane):
        '''Adds a new airplane to the airplane string'''
        airplane_stream = open('./repo/Airplane.csv', 'a')
        airplane_str = airplane.raw_info()
        airplane_stream.write(airplane_str)
        airplane_stream.close()
        return    

    def pull_airplane_types_info(self):
        # Ath!!
        airplane_stream = open("./repo/AirplaneType.csv", "r")
        self.airplanes_types_list = []
        new_airplane_type_list = []
        
        for airplane in airplane_stream:
            check_list = []
            new_airplane_type = self.__modelAPI.get_model("AirplaneType")
            self.airplanes_types_list = airplane.strip().split(",")
            check_list.append(new_airplane_type.set_plane_type_id(self.airplanes_types_list[self.PLANE_TYPE_ID]))
            check_list.append(new_airplane_type.set_make(self.airplanes_types_list[self.PLANE_TYPE_MAKE]))
            check_list.append(new_airplane_type.set_model(self.airplanes_types_list[self.PLANE_TYPE_MODEL]))
            check_list.append(new_airplane_type.set_capacity(self.airplanes_types_list[self.PLANE_TYPE_CAPACITY]))      
            if False not in check_list:
                new_airplane_type_list.append(new_airplane_type)
        airplane_stream.close()
        return new_airplane_type_list

    def push_all_airplanes(self, airplane_list):

        HEADER = "planeTypeId,planeInsignia\n"
        filestream = open("./repo/Airplane_temp.csv", "a")
        filestream.write(HEADER)
        for airplane_info in airplane_list:
            filestream.write(airplane_info.raw_info())
        filestream.close()
        os.remove("./repo/Airplane.csv")
        os.rename("./repo/Airplane_temp.csv", "./repo/Airplane.csv")
        return