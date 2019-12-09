from datetime import datetime

class LLAirplanes:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_airplane_list = []

    def validate_airplane(self, airplane):
        '''Gets airplane instance and returns a boolean'''
        return self.__modelAPI.validate_model(airplane)

    def get_all_airplane_list(self):
        '''Gets a list of instances of airplanes and returns it'''
        return self.__dl_api.pull_all_airplanes()

    def get_airplane_type_list(self):
        '''Gets a list of instances of airplane types and returns it'''
        return self.__dl_api.pull_all_airplane_types()
    
    def create_airplane(self, airplane, airplane_types,insignia):
        '''Gets a list of airplane instances, checks if user created instance exists in list, returns boolean and instance'''
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

    def overwrite_all_airplanes(self, airplane_list):
        return self.__dl_api.overwrite_all_airplanes(airplane_list)

    def get_airplane_status(self, all_airplane_list):

        all_voyage_list = self.__dl_api.pull_all_voyages()
        current_date = datetime.now().replace(microsecond=0).isoformat()
        current_voyages = []

        for voyage in all_voyage_list:
            first_flight_start = voyage.get_departing_flight_departure_date()
            second_flight_end = voyage.get_return_flight_arrival_date()

            if first_flight_start <= current_date <= second_flight_end:
                current_voyages.append(voyage)
                
        for airplane in all_airplane_list:
            for voyage in current_voyages:

                if voyage.get_departing_flight_departure_date() <= current_date <= voyage.get_departing_flight_arrival_date():
                    airplane.set_status("In air, departing")
                elif voyage.get_departing_flight_arrival_date() <= current_date <= voyage.get_return_flight_departure_date():
                    airplane.set_status("At destination")
                elif voyage.get_return_flight_departure_date() <= current_date <= voyage.get_return_flight_arrival_date():
                    airplane.set_status("In air, returning")

        
