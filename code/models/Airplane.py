from validation.validator import Validator

models_validation = Validator()


class Airplane():


    def __init__(self, name='', make='', model='', max_seats=0):
        self.__name = name
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats


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
        if models_validation.validate_airplane_make:
            self.__make = new_make
        else:
            pass

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        if models_validation.validate_airplane_model:
            self.__model = new_model
        else:
            pass

    def get_max_seats(self):
        return self.__max_seats

    def set_max_seats(self, new_max_seats):
        if models_validation.validate_airplane_max_seats:
            self.__max_seats = new_max_seats
        else:
            pass
