class Employee():
    def __init__(self, name = '', ssn = '', address = '', \
        home_num = 0, mobile_num = 0, email = '', title = ''):
        self.__id = get_id()
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title

    def get_id(self):
        pass

class Pilot(Employee):
    def __init__(self, airplane_type = ''):
        self.__airplane_type = airplane_type
        pass

class FlightAttendant(Employee):
    def __init__(self):
        pass
class Voyage():
    def __init__(self):
        self.__id = get_id()
        self.__destination = get_destination()
        self.__airplane = get_airplane()
        self.__departure = get_flight()
        self.__return = get_flight()
        self.__pilot = get_pilot()
        self.__co_pilot = get_pilot()
        self.__purser = get_flight_attendant()
        self.__cabin_crew_list = get_flight_attendant_list()
        self.__status = ''

    def get_id(self):
        pass
    def get_destination(self):
        pass
    def get_airplane(self):
        pass
    def get_flight(self):
        pass
    def get_pilot(self):
        pass
    def get_flight_attendant(self):
        pass
    def get_flight_attendant_list(self):
        pass
    def generate_flight_number(self):
        pass


class Airplane():
    def __init__(self, name = '', make = '', model = '', max_seats = 0):
        self.__id = get_id()
        self.__name = name
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats

    def get_id(self):
        pass

class Destination():
    def __init__(self, country = '', airport = '', flight_time = '', distance = '', contact_name = '', contact_num = 0):
        self.__id = get_id()
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_num = contact_num

    def get_id(self):
        pass

class Flight():
    def __init__(self, departure_airport = '', arrival_airport = '', \
        departure_date = '', departure_time = '', arrival_date = '', arrival_time = ''):
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_date = departure_date
        self.__departure_time = departure_time
        self.__arrival_date = arrival_date
        self.__arrival_time = arrival_time

