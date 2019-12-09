from validation.validator import Validator
class Airplane():

    def __init__(self, name='', make='', model='', max_seats=0, availability = "",current_destination = "", flight_number = "", date_available = ""):
        self.__models_validation = Validator()
        self.__name = name #insignia
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats
        
        self.__create_validation_dict = {self.get_name:self.set_name}

        self.__create_order_list = ["airplane insignia"]

        self.__availability = availability
        self.__current_destination = current_destination
        self.__flight_number = flight_number
        self.__date_available = date_available



    def __str__(self):
        return "Insignia {:>2}\nMake: {:>2}\nModel: {:>2}\nMaximum seats: {:>2}".format(self.__name, self.__make, self.__model, self.__max_seats)

    def raw_info(self):
        return "NA" + self.__make + self.__model + "," + self.__name + "\n"

    def set_availability(self, availability):
        self.__availability = availability
    
    def get_availability(self):
        return self.__availability
    
    def set_current_destination(self, destination):
        self.__current_destination = destination
    
    def get_current_destination(self):
        return self.__current_destination

    def set_flight_number(self,flight_number):
        self.__flight_number = flight_number
    def get_flight_number(self):
        return self.__flight_number
    
    def set_date_available(self, date):
        self.__date_available = date
    
    def get_date_available(self):
        return self.__date_available

    def get_create_validation_dict(self):
        return self.__create_validation_dict

    def get_create_order_list(self):
        return self.__create_order_list
    
    def handle_key_value(self, key, value):
        return value(key())

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


    def get_model_header_format(self, header_flag):
        return "{:10}{:11}{:11}{:11}{:15}{:12}{:17}{:17}{:18}".format("Index: ",
                                                                    "Name:",
                                                                    "Make:",
                                                                    "Model:",
                                                                    "Total seats:",
                                                                    "Status:",
                                                                    "Destination:",
                                                                    "Flight number:",
                                                                    "Date available:")
    def get_model_list_info(self, header_flag):
        returnObject = ("     {:11}{:11}{:11}{:15}{:12}{:17}{:17}{:18}|\n".format(
                                                                      self.get_name(),
                                                                      self.get_make(),
                                                                      self.get_model(),
                                                                      self.get_max_seats(),
                                                                      "status",
                                                                      "destination",
                                                                      "flight_num",
                                                                      "date_avail"))
        return returnObject
