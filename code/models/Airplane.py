from validation.validator import Validator

models_validation = Validator()


class Airplane():

    def __init__(self, an_id='', name='', make='', model='', max_seats=0):
        self.__id = an_id
        self.__name = name
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats

    def __str__(self):
        return "Country: {:>2}\nAirport: {:>2}\nFlight time: {:>2}\nDistance: {:>2}\nContact name: {:>2}\nContact number: {:>2}".format(self.__country, self.__airport, self.__flight_time, self.__distance, self.__contact_name, self.__contact_num)


    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if models_validation.validate_airplane_name:
            self.__name = new_name
        else:
            pass

    def get_make(self):
        return self.__make

    def set_make(self, new_make):
        # if models_validation.validate_airplane_make:
        #     self.__make = new_make
        # else:
        #     pass
        pass

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        # if models_validation.validate_airplane_model:
        #     self.__model = new_model
        # else:
        #     pass
        pass
    def get_max_seats(self):
        return self.__max_seats

    def set_max_seats(self, new_max_seats):
        # if models_validation.validate_airplane_max_seats:
        #     self.__max_seats = new_max_seats
        # else:
        #     pass
        pass
