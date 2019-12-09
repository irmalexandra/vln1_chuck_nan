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
        self.__all_airplane_list = self.__dl_api.pull_all_airplanes()
        self.get_airplane_status()
        '''Gets a list of instances of airplanes and returns it'''
        return self.__all_airplane_list

    def get_airplane_type_list(self):
        '''Gets a list of instances of airplane types and returns it'''
        return self.__dl_api.pull_all_airplane_types()
    
    def create_airplane(self, airplane, airplane_types,insignia):
        '''Gets a list of airplane instances, checks if user created instance exists in list, returns boolean and instance'''
        self.__all_airplane_list = self.get_all_airplane_list()
        existing_airplanes_list = [x.get_insignia() for x in self.__all_airplane_list]
        if airplane.get_insignia() not in existing_airplanes_list:
            existing_airplane_types = airplane_types
            airplane_make = airplane.get_make()
            airplane_model = airplane.get_model()
            
            for info in existing_airplane_types:
                if info.get_make() == airplane_make and info.get_model() == airplane_model:
                    airplane.set_capacity(info.get_capacity())
                    self.__dl_api.create_airplane(airplane)

                    return  airplane,True
        return airplane,False

    def overwrite_all_airplanes(self, airplane_list):
        return self.__dl_api.overwrite_all_airplanes(airplane_list)

    def filter_available_airplanes(self, voyage):

        all_airplane_list = self.get_all_airplane_list()
        
        start_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
        end_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

        self.get_airplane_status(start_date)

        available_airplane_list = []
        all_voyage_list = self.__dl_api.pull_all_voyages()

        for airplane in all_airplane_list:
            if airplane not in available_airplane_list:
                for voyage in all_voyage_list:
                    if airplane in available_airplane_list:
                        break
                    other_start_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
                    other_end_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

                    if start_date > other_end_date or end_date < other_start_date:
                        available_airplane_list.append(airplane)

        return available_airplane_list

    def get_airplane_status(self, current_date = datetime.now().replace(microsecond=0).isoformat()):

        all_voyage_list = self.__dl_api.pull_all_voyages()
        
        current_voyages = []

        for voyage in all_voyage_list:
            dep_flight_start = voyage.get_departing_flight_departure_date()
            ret_flight_end = voyage.get_return_flight_arrival_date()

            if dep_flight_start <= current_date <= ret_flight_end:
                current_voyages.append(voyage)
                
        for airplane in self.__all_airplane_list:
            for voyage in current_voyages:
                dep_flight_start = voyage.get_departing_flight_departure_date()
                dep_flight_end = voyage.get_departing_flight_arrival_date()
                ret_flight_start = voyage.get_return_flight_departure_date()
                ret_flight_end = voyage.get_return_flight_arrival_date()

                if airplane.get_insignia() == voyage.get_airplane_insignia():
                    airplane.set_current_destination(voyage.get_return_flight_departing_from())
                    airplane.set_date_available(ret_flight_end)

                    if dep_flight_start <= current_date <= dep_flight_end:
                        airplane.set_flight_number(voyage.get_departing_flight_num())
                        airplane.set_availability("In air, departing")

                    elif dep_flight_end <= current_date <= ret_flight_start:
                        airplane.set_flight_number("N/A")
                        airplane.set_availability("At destination")

                    elif ret_flight_start <= current_date <= ret_flight_end:
                        airplane.set_flight_number(voyage.get_return_flight_num())
                        airplane.set_availability("In air, returning")

        
    def get_iso_format_date_time(self, date=''):

        if date.find("T") == -1:
            date = datetime.strptime(date,'%d-%m-%Y')
        else:
            date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')

        return date