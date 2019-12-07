from validation.validator import Validator
class Destination():
    def __init__(self, country='', airport='', flight_time='', distance='', contact_name='', contact_number=0):
        self.__models_validation = Validator()
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_number = contact_number

        self.__validation_dict = {self.get_contact_name:self.set_contact_name, self.get_contact_number:self.set_contact_number}

        self.__creation_order_list = ["contact name", "contact number"]

    def __str__(self):
        return "Country: {:>2}\nAirport: {:>2}\nFlight time: {:>2}\nDistance: {:>2}\nContact name: {:>2}\nContact numberber: {:>2}".format(self.__country, self.__airport, self.__flight_time, self.__distance, self.__contact_name, self.__contact_number)

    def raw_info(self):
        return self.__country + "," + self.__airport + "," + self.__flight_time + "," + self.__distance + "," + self.__contact_name + "," + self.__contact_number + "\n"

    def get_validation_dict(self):
        return self.__validation_dict

    def get_creation_order_list(self):
        return self.__creation_order_list

    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        if self.__models_validation.validate_country(new_country):
            self.__country = new_country
        else:
            pass

    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        if self.__models_validation.validate_airport(new_airport):
            self.__airport = new_airport

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        if self.__models_validation.validate_flight_time(new_flight_time):
            self.__flight_time = new_flight_time
        else:
            pass

    def get_distance(self):
        return self.__distance

    def set_distance(self, new_distance):
        if self.__models_validation.validate_distance(new_distance):
            self.__distance = new_distance
        else:
            pass

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
