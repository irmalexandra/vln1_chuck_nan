from validation.validator import Validator
class Airplane():

    def __init__(self, insignia='', make='', model='', capacity=0):
        self.__models_validation = Validator()
        self.__insignia = insignia
        self.__make = make
        self.__model = model
        self.__capacity = capacity
        
        self.__create_validation_dict = {self.get_insignia:self.set_insignia}

        self.__create_order_list = ["airplane insignia"]

        self.__availability = "Not in use"
        self.__current_destination = "Reykjavik"
        self.__flight_number = "N/A"
        self.__date_available = "N/A"


    def __str__(self):
        return "Insignia {:>2}\nMake: {:>2}\nModel: {:>2}\nMaximum seats: {:>2}".format(self.__insignia, self.__make, self.__model, self.__capacity)

    def raw_info(self):
        return "NA" + self.__make + self.__model + "," + self.__insignia + "\n"

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

    def get_insignia(self):
        return self.__insignia

    def set_insignia(self, new_insignia):
        if self.__models_validation.validate_airplane_insignia(new_insignia):
            self.__insignia = new_insignia
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

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, new_capacity):
        if self.__models_validation.validate_airplane_capacity(new_capacity):
            self.__capacity = new_capacity
            return True
        else:
            return False

    def change_date_time_format(self, date_string):
        date_string = date_string[:-3].replace("T", " ")
        return date_string

    def get_model_header_format(self, header_flag):
        return "{:10}{:12}{:10}{:10}{:12}{:18}{:16}{:17}{:18}".format("Index: ",
                                                                    "Insignia:",
                                                                    "Make:",
                                                                    "Model:",
                                                                    "Capacity:",
                                                                    "Status:",
                                                                    "Destination:",
                                                                    "Flight number:",
                                                                    "Date available:")
    def get_model_list_info(self, header_flag):
        returnObject = ("     {:12}{:10}{:10}{:12}{:18}{:16}{:17}{:18}|\n".format(
                                                                      self.get_insignia(),
                                                                      self.get_make(),
                                                                      self.get_model(),
                                                                      self.get_capacity(),
                                                                      self.get_availability(),
                                                                      self.get_current_destination(),
                                                                      self.get_flight_number(),
                                                                      self.change_date_time_format(self.get_date_available())))
        return returnObject

