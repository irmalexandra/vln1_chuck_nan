
class LLAirplanes:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_airplane_list = []

    def validate_airplane(self, airplane):
        ''' Gets airplane instance and returns a boolean '''
        return self.__modelAPI.validate_model(airplane)

    def get_all_airplane_list(self):
        ''' Gets a list of instances of airplanes and returns it '''
        return self.__dl_api.pull_all_airplanes()

    def get_airplane_type_list(self):
        ''' Gets a list of instances of airplane types and returns it '''
        return self.__dl_api.pull_all_airplane_types()
    
    def create_airplane(self, airplane, airplane_types,insignia):
        ''' Gets a list of airplane instances, checks if user created instance exists in list, returns boolean and instance '''
        self.__all_airplane_list = self.get_all_airplane_list()
        existing_airplanes_list = [x.get_name() for x in self.__all_airplane_list]
        if airplane.get_name() not in existing_airplanes_list:
            existing_airplane_types = airplane_types
            airplane_make = airplane.get_make()
            airplane_model = airplane.get_model()
            
            for info in existing_airplane_types:
                if info.get_make() == airplane_make and info.get_model() == airplane_model:
                    airplane.set_max_seats(info.get_capacity())
                    self.__dl_api.create_airplane(airplane)

                    return  airplane,True
        return airplane,False


        
