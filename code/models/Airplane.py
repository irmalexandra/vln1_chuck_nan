from validation.validator import Validator
class Airplane():

    def __init__(self, name='', make='', model='', max_seats=0):
        self.__models_validation = Validator()
        self.__name = name #insignia
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats
        
        self.__validation_dict = {self.get_name:self.set_name}

        self.__creation_order_list = ["airplane insignia"]

    def __str__(self):
        return "ID: {:>2}\nMake: {:>2}\nModel: {:>2}\nMaximum seats: {:>2}".format(self.__name, self.__make, self.__model, self.__max_seats)

    def raw_info(self):
        return "NA" + self.__make + self.__model + "," + self.__name + "\n"

    def get_validation_dict(self):
        return self.__validation_dict

    def get_creation_order_list(self):
        return self.__creation_order_list

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__models_validation.validate_airplane_insignia(new_name):
            self.__name = new_name
            return True
        else:
            return False

    def get_make(self):
        return self.__make

    def set_make(self, new_make):
        if self.__models_validation.validate_airplane_make(new_make):
            self.__make = new_make
            return True
        else:
            return False

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        if self.__models_validation.validate_airplane_model(new_model):
            self.__model = new_model
            return True
        else:
            return False

    def get_max_seats(self):
        return self.__max_seats

    def set_max_seats(self, new_max_seats):
        if self.__models_validation.validate_airplane_capacity(new_max_seats):
            self.__max_seats = new_max_seats
            return True
        else:
            return False
