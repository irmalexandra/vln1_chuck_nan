from validation.validator import Validator

models_validation = Validator()


class Airplane():
    PLANE_TYPE_ID = 0
    PLANE_INSIGNIA = 1

    ID = 3

    def __init__(self, a_id, name='', make='', model='', max_seats=0):
        self.__id = a_id
        self.__name = name
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats

    def __str__(self):
        return "id: {:<2} name: {:>2} ssn: {:>2} address: {:>2} home number: {:>2} mobile number: {:>2} email: {:>2} title: {:>2} rank: {:>2}".format(self.__id, self.__name, self.__ssn, self.__address, self.__home_num, self.__mobile_num, self.__email, self.__title, self.__rank)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if models_validation.validate_airplane_id:
            self.__id = new_id
        else:
            pass

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
