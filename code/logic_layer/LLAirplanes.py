from datetime import datetime

class LLAirplanes:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_airplane_list = []
        self.__all_airplane_type_list = []

    # All list functions

    def get_all_airplane_list(self):
        '''Gets a list of instances of airplanes and returns it'''
        if not self.__all_airplane_list:
            self.__all_airplane_list = self.__dl_api.pull_all_airplanes()

        self.get_airplane_status()
        
        return self.__all_airplane_list

    def get_airplane_type_list(self):
        '''Gets a list of instances of airplane types and returns it'''
        self.__all_airplane_type_list = self.__dl_api.pull_all_airplane_types()
        return self.__all_airplane_type_list
    
    def filter_available_airplanes(self, voyage):

        all_airplane_list = self.get_all_airplane_list()
        
        selected_voyage_start_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
        selected_voyage_end_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

        self.get_airplane_status(selected_voyage_start_date)

        available_airplane_list = []
        unavailable_voyages = []
        unavailable_airplane_insignias = []

        all_voyage_list = self.__dl_api.pull_all_voyages()

        for voyage in all_voyage_list:        
            voyage_start_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
            voyage_end_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

            if selected_voyage_start_date <= voyage_start_date <= selected_voyage_end_date \
                or selected_voyage_start_date <= voyage_end_date <= selected_voyage_end_date:
                unavailable_voyages.append(voyage)

            elif voyage_start_date <= selected_voyage_start_date <= voyage_end_date \
                or voyage_start_date <= selected_voyage_end_date <= voyage_end_date:
                unavailable_voyages.append(voyage)


        for voyage in unavailable_voyages:
            unavailable_airplane_insignias.append(voyage.get_airplane_insignia())

        for airplane in all_airplane_list:
            if airplane.get_insignia() in unavailable_airplane_insignias:
                continue
            else:
                available_airplane_list.append(airplane)

        return available_airplane_list

    # All change functions

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
                    if self.__modelAPI.validate_model(airplane):
                        return self.__dl_api.append_airplane(airplane)
        return False

    def overwrite_all_airplanes(self, airplane_list):
        return self.__dl_api.overwrite_all_airplanes(airplane_list)

    # All special functions

    def get_airplane_status(self, current_date = datetime.now().replace(microsecond=0)):

        for airplane in self.__all_airplane_list:
            airplane.set_status("Not in use")
            airplane.set_current_destination("N/A")
            airplane.set_date_available("N/A")
            airplane.set_flight_number("N/A")

        all_voyage_list = self.__dl_api.pull_all_voyages()
        
        current_voyages = []

        for voyage in all_voyage_list:
            dep_flight_start = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
            ret_flight_end = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

            if dep_flight_start <= current_date <= ret_flight_end:
                current_voyages.append(voyage)
                
        for airplane in self.__all_airplane_list:
            for voyage in current_voyages:
                dep_flight_start = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
                dep_flight_end = self.get_iso_format_date_time(voyage.get_departing_flight_arrival_date())
                ret_flight_start = self.get_iso_format_date_time(voyage.get_return_flight_departure_date())
                ret_flight_end = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

                if airplane.get_insignia() == voyage.get_airplane_insignia():
                    airplane.set_current_destination(voyage.get_return_flight_departing_from())
                    airplane.set_date_available(ret_flight_end.isoformat())

                    if dep_flight_start <= current_date <= dep_flight_end:
                        airplane.set_flight_number(voyage.get_departing_flight_num())
                        airplane.set_status("In air, departing")

                    elif dep_flight_end <= current_date <= ret_flight_start:
                        airplane.set_flight_number("N/A")
                        airplane.set_status("At destination")

                    elif ret_flight_start <= current_date <= ret_flight_end:
                        airplane.set_flight_number(voyage.get_return_flight_num())
                        airplane.set_status("In air, returning")

    def get_iso_format_date_time(self, date = "00-00-0000", time = "00:00:00"):
        if type(date).__name__ != 'datetime':

            if date.find("T") == -1:
                new_date = datetime.strptime(date,'%d-%m-%Y')
                new_time = datetime.strptime(time, '%H:%M:%S').time()
                new_date = datetime.combine(new_date, new_time)
            else:
                new_date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
            return new_date
        return date