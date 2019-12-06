
class LLAirplanes:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__existing_airplanes = []

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.__dl_api.pull_all_airplanes()

    def pull_airplane_types(self):
        return self.__dl_api.pull_all_airplane_types()
    
    def create_airplane(self, airplane, airplane_types,insignia):

        self.__existing_airplanes = self.get_all_airplanes()
        existing_airplanes_list = [x.get_name() for x in self.__existing_airplanes]
        if airplane.get_name() not in existing_airplanes_list:
            existing_airplane_types = airplane_types
            airplane_make = airplane.get_make()
            airplane_model = airplane.get_model()
            #need to see if plane already exist or na!
            for info in existing_airplane_types:
                if info.get_make() == airplane_make and info.get_model() == airplane_model:
                    airplane.set_max_seats(info.get_capacity())
                    self.__dl_api.create_airplane(airplane)

                    return  airplane,True
        return airplane,False


        
