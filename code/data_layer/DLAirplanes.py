class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    AIRPLANE_DICT_PLANE_TYPE = 0
    AIRPLANE_DICT_MODEL = 1
    AIRPLANE_DICT_CAPACITY = 2

    def __init__(self, modelAPI):
        self.all_airplanes_list = []
        self.__modelAPI = modelAPI

    def clear_airplane_list(self):
        self.all_airplanes_list.clear()


    def pull_all_airplanes(self):
        '''Opens csv files and returns a list of all the airplanes (type ID, name, type)'''
        airplane_stream = open("./repo/Airplane.csv", "r")
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
        filestream = open("./repo/AirplaneType.csv", "r")
        airplanes_list = []
        new_airplane_type = self.modelAPI.get_model("AirplaneType")
        for airplane in filestream:
            airplanes_list.append(airplane.strip())
        filestream.close()
        return airplanes_list[1:]