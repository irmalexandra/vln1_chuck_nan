from validation.validator import Validator

models_validation = Validator()


class Voyage():
    def __init__(self):
        self.__destination = get_destination()
        self.__airplane = get_airplane()
        self.__departure = get_flight_departure()
        self.__return = get_flight_return()
        self.__pilot = get_pilot()
        self.__co_pilot = get_pilot()
        self.__fsm = get_flight_attendant()
        self.__cabin_crew_list = get_flight_attendant_list()
        self.__status = ''

    def __str__(self):
        return "Destination: {:>2} \nAirplane: {:>2} \nDeparture: {:>2} \nReturn: {:>2} \nPilot: {:>2} \nCo-pilot: {:>2} \nFlight service manager: {:>2} \nCabin crew: {:>2} \nStatus: ".format(self.__destination, self.__airplane, self.__departure, self.__return, self.__pilot, self.__co_pilot, self.__fsm, self.__cabin_crew_list, self.__status)
