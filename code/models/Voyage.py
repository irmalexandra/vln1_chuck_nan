from validation import *

models_validation = Validator()


class Voyage():
    def __init__(self):
        self.__id = get_id()
        self.__destination = get_destination()
        self.__airplane = get_airplane()
        self.__departure = get_flight_departure()
        self.__return = get_flight_return()
        self.__pilot = get_pilot()
        self.__co_pilot = get_pilot()
        self.__purser = get_flight_attendant()
        self.__cabin_crew_list = get_flight_attendant_list()
        self.__status = ''
