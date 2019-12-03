from validation import *

models_validation = Validator()

class Voyage():
    def __init__(self):
        self.__id = self.get_id()
        self.__destination = self.get_destination()
        self.__airplane = self.get_airplane()
        self.__departure = self.get_flight_departure()
        self.__return = self.get_flight_return()
        self.__pilot = self.get_pilot()
        self.__co_pilot = self.get_pilot()
        self.__purser = self.get_flight_attendant()
        self.__cabin_crew_list = self.get_flight_attendant_list()
        self.__status = ''

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if models_validation.validate_voyage_id:
            self.__id = new_id
        else:
            pass

    def get_destination(self):
        return self.__destination

    def set_destination(self, new_destination):
        if models_validation.validate_voyage_destination:
            self.__destination = new_destination
        else:
            pass

    def get_airplane(self):
        return self.__airplane

    def set_airplane(self, new_airplane):
        if models_validation.validate_voyage_airplane:
            self.__airplane = new_airplane
        else:
            pass

    def get_flight_departure(self):
        return self.__departure

    def set_flight_departure(self, new_flight_departure):
        if models_validation.validate_voyage_flight_departure:
            self.__flight_departure = new_flight_departure
        else:
            pass

    def get_flight_return(self):
        return self.__return

    def set_flight_return(self, new_flight_return):
        if models_validation.validate_voyage_flight_return:
            self.__flight_return = new_flight_return
        else:
            pass

    def get_pilot(self):
        return self.__pilot

    def set_pilot(self, new_pilot):
        if models_validation.validate_voyage_pilot:
            self.__pilot = new_pilot
        else:
            pass

    def get_flight_attendant(self):
        return self.__purser

    def set_flight_attendant(self, new_flight_attendant):
        if models_validation.validate_voyage_flight_attendant:
            self.__flight_attendant = new_flight_attendant
        else:
            pass

    def get_flight_attendant_list(self):
        return self.__cabin_crew_list

    def set_flight_attendant_list(self, new_flight_attendant_list):
        if models_validation.validate_voyage_flight_attendant_list:
            self.__flight_attendant_list = new_flight_attendant_list
        else:
            pass

    def generate_flight_number(self):
        return
