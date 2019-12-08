from datetime import datetime

class LLVoyages:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_voyage_list = []

    def validate_voyage(self, voyage):
        ''' Gets voyage instance and returns a boolean '''
        return self.__modelAPI.validate_model(voyage)

    def get_voyage(self, voyage_ID):
        pass

    def get_all_voyage_list(self):
        return self.__dl_api.pull_all_voyages()

    def overwrite_all_voyages(self, voyage_list):
        return self.__dl_api.overwrite_all_voyages(voyage_list)

    def filter_all_empty_voyages(self):
        '''Takes a list of all voyage instances and returns a list of filtered voyage instances'''
        self.__all_voyage_list = self.get_all_voyage_list() 
        empty_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_airplane_insignia == ".":
                empty_voyage_list.append(voyage)

        return empty_voyage_list

    def filter_all_voyages_by_period(self, start_date, end_date):
        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")

        start = datetime(start_year, start_month, start_day)
        end = datetime(end_year, end_month, end_day)

        self.__all_voyage_list = self.get_all_voyage_list() 
        period_voyage_list = []

        for voyage in self.__all_voyage_list:
            if start <= voyage.get_return_flight_arrival_date() or voyage.get_departing_flight_departing_date() <= end:
                period_voyage_list.append(voyage)
        return period_voyage_list
        
    def filter_all_voyages_by_destination(self, airport):

        self.__all_voyage_list = self.get_all_voyage_list()
        destination_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_destination() == airport:
                destination_voyage_list.append(voyage)

        return destination_voyage_list

    def duplicate_voyage(self, voyage, date_time):
        destination = voyage.get_destination()
        new_voyage = self.__modelAPI.get_model("Voyage")

        new_voyage.set_destination(destination)
        new_voyage.set_departing_flight_departure_date(date_time)

        voyage.set_flight_numbers(self.generate_flight_numbers())
        voyage.set_flight_times(self.calculate_flight_times(voyage, date_time))

        return self.__dl_api.append_voyage(voyage)

    def repeat_voyage(self, voyage, repeat_interval, end_date):
        date = voyage.get_departing_flight_departing_date()
        while date <= end_date:
            date =+ repeat_interval
            self.duplicate_voyage(voyage, date)

    def populate_voyage(self):
        pass

    def generate_flight_numbers(self):
        pass

    def calculate_flight_times(self):
        pass

    def get_iso_format_date_time(self, date, time):

        time = datetime.strptime(time,'%H:%M:%S').time()
        date = datetime.strptime(date,'%d-%m-%Y').date()

        return datetime.combine(date, time)