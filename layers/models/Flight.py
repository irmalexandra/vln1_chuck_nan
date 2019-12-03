from validation import *

models_validation = Validator()

class Flight():
    def __init__(self, departure_airport='', arrival_airport='',
                 departure_date_time='', arrival_date_time=''):
        self.__id = self.get_id()
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_date_time = departure_date_time
        self.__arrival_date_time = arrival_date_time

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if models_validation.validate_flight_id:
            self.__id = new_id
        else:
            pass

    def get_departure_airport(self):
        return self.__departure_airport

    def set_departure_airport(self, new_departure_airport):
        if models_validation.validate_flight_departure_airport:
            self.__departure_airport = new_departure_airport
        else:
            pass

    def get_arrival_airport(self):
        return self.__arrival_airport

    def set_arrival_airport(self, new_arrival_airport):
        if models_validation.validate_flight_arrival_airport:
            self.__arrival_airport = new_arrival_airport
        else:
            pass

    def get_departure_date_time(self):
        return self.__departure_date_time

    def set_departure_date_time(self, new_departure_date_time):
        if models_validation.validate_flight_departure_date_time:
            self.__departure_date_time = new_departure_date_time
        else:
            pass

    def get_arrival_date_time(self):
        return self.__arrival_airport

    def set_arrival_date_time(self, new_arrival_date_time):
        if models_validation.validate_flight_arrival_date_time:
            self.__arrival_date_time = new_arrival_date_time
        else:
            pass
