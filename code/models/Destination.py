from validation.validator import Validator
class Destination():
    def __init__(self, destination_id = 0, country = '', airport = '', flight_time = '', 
                 distance = '', contact_name = '', contact_number = ''):
        self.__models_validation = Validator()
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_number = contact_number
        self.__destination_id = destination_id

        self.__header_format_dict = {"default": self.get_model_header_default_format}

        self.__list_info_dict = {"default": self.get_model_list_default_info}

        self.__validation_dict = {self.get_country: self.set_country, 
                                         self.get_airport: self.set_airport,
                                         self.get_flight_time: self.set_flight_time,
                                         self.get_distance: self.set_distance,
                                         self.get_contact_name: self.set_contact_name,
                                         self.get_contact_number: self.set_contact_number}

        self.__create_order_list = [
            "country", "airport", "flight time", "distance", "contact name", "contact number"]
        
        self.__creation_dict = {"country": self.set_country,
                                "airport": self.set_airport,
                                "flight time": self.set_flight_time,
                                "distance": self.set_distance,
                                "contact name": self.set_contact_name,
                                "contact number": self.set_contact_number 
        }

    def __str__(self):
        return "Country: {:>2}\nAirport: {:>2}\nFlight time: {:>2}\nDistance: {:>2}\nContact name: {:>2}\nContact numberber: {:>2}".format(self.__country, self.__airport, self.__flight_time, self.__distance, self.__contact_name, self.__contact_number)

    def get_creation_process(self):
        return self.__create_order_list, self.__creation_dict
    
    def get_model_header_format(self, header_flag):
        return self.__header_format_dict[header_flag]()

    def get_model_list_info(self, header_flag):
        return self.__list_info_dict[header_flag]()
    
    
    def get_model_header_default_format(self):
        return "{:10}{:20}{:17}{:20}{:15}{:22}{:34}".format("Index:",
                                                          "Country:",
                                                          "Airport:",
                                                          "Flight time:",
                                                          "Distance:",
                                                          "Contact name:",
                                                          "Contact number:")
        
    def get_model_list_default_info(self):
        returnObject = "     {:20}{:17}{:20}{:15}{:22}{:34}|\n".format(
                                                                      self.get_country(),
                                                                      self.get_airport(),
                                                                      self.get_flight_time(),
                                                                      self.get_distance(),
                                                                      self.get_contact_name(),
                                                                      self.get_contact_number())
        return returnObject

    def raw_info(self):
        return self.__country + "," + self.__airport + "," + self.__flight_time + "," + self.__distance + \
            "," + self.__contact_name + "," + self.__contact_number + "," + self.__destination_id + "\n"

    def get_validation_dict(self):
        return self.__validation_dict

    def get_create_order_list(self):
        return self.__create_order_list

    def handle_key_value(self, key, value):
        return value(key())    

    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        if self.__models_validation.validate_country(new_country):
            self.__country = new_country
            return True
        return False

    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        if self.__models_validation.validate_airport(new_airport):
            self.__airport = new_airport
            return True
        return False

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        if self.__models_validation.validate_flight_time(new_flight_time):
            self.__flight_time = new_flight_time
            return True
        else:
            return False

    def get_distance(self):
        return self.__distance

    def set_distance(self, new_distance):
        if self.__models_validation.validate_distance(new_distance):
            self.__distance = new_distance
            return True
        else:
            return False

    def get_contact_name(self):
        return self.__contact_name

    def set_contact_name(self, new_contact_name):
        if self.__models_validation.validate_contact_name(new_contact_name):
            self.__contact_name = new_contact_name
            return True
        else:
            return False

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, new_contact_number):
        if self.__models_validation.validate_contact_number(new_contact_number):
            self.__contact_number = new_contact_number
            return True
        else:
            return False

    def get_destination_id(self):
        return self.__destination_id

    def set_destination_id(self, new_id):
        if self.__models_validation.validate_id(new_id):
            self.__destination_id = new_id
            return True
        return False