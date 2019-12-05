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

    def pull_airplane_types(self):
        return self.__dl_api.populate_all_airplane_types()
    
    def create_airplane(self, airplane, airplane_types):
        existing_airplane_types = airplane_types
        airplane_make = airplane.get_make()
        airplane_model = airplane.get_model()
        make = None 
        model = None 
        for info in existing_airplane_types:
            info_list = info.split(",")

            if info_list[self.MAKE] == airplane_make and info_list[self.MODEL] == airplane_model:
                airplane.set_max_seats(info_list[self.CAPACITY])
                self.__dl_api.create_airplane(airplane)
                make = True
                model = True
                return make, model, airplane


            elif airplane_make == info_list[self.MAKE] and airplane_model != info_list[self.MODEL]:
                model = False


            elif airplane_make != info_list[self.MAKE] and airplane_model == info_list[self.MODEL]:
                make = False 

        return make, model, airplane
        
