class LLAirplanes:
    MAKE = 1
    MODEL = 2
    CAPACITY = 3
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.__dl_api.populate_all_airplanes()
    
    def create_airplane(self, airplane):
        existing_airplanes = self.__dl_api.populate_all_airplane_types()
        airplane_make = airplane.get_make()
        airplane_model = airplane.get_model()
        print(existing_airplanes)
        for info in existing_airplanes:
            info_list = info.split(",")
            print(info_list[self.MAKE],airplane_make,info_list[self.MODEL],airplane_model, "<----")
            if info_list[self.MAKE] == airplane_make and info_list[self.MODEL] == airplane_model:
                print("yays")
                airplane.set_max_seats(info_list[self.CAPACITY])
        

        print(airplane)
        self.__dl_api.create_airplane(airplane)
