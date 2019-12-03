from validation.validator import Validator

models_validation = Validator()


class Destination():
    def __init__(self, country='', city='', airport='', flight_time='', distance='', contact_name='', contact_number=0):
        self.__country = country
        self.__city = city
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_number = contact_number

    def __str__(self):
        return "Country: {:>2}\nCity: {:>2}\nAirport: {:>2}\nFlight time: {:>2}\nDistance: {:>2}\nContact name: {:>2}\nContact numberber: {:>2}".format(self.__country, self.__city, self.__airport, self.__flight_time, self.__distance, self.__contact_name, self.__contact_number)

    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        if models_validation.validate_country:
            self.__country = new_country
        else:
            pass

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        if models_validation.validate_city:
            self.__city = new_city
        else:
            pass

    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        if models_validation.validate_airport:
            self.__airport = new_airport
        else:
            pass

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        if models_validation.validate_flight_time:
            self.__flight_time = new_flight_time
        else:
            pass

    def get_distance(self):
        return self.__distance

    def set_distance(self, new_distance):
        if models_validation.validate_distance:
            self.__distance = new_distance
        else:
            pass

    def get_contact_name(self):
        return self.__contact_name

    def set_contact_name(self, new_contact_name):
        if models_validation.validate_contact_name:
            self.__contact_name = new_contact_name
        else:
            pass

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, new_contact_number):
        if models_validation.validate_contact_number:
            self.__contact_number = new_contact_number
        else:
            pass
