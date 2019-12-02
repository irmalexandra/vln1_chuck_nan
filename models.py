from validation import *


class Employee():
    def __init__(self, name='', ssn='', address='', home_num=0, mobile_num=0, email='', title=''):
        self.__id = self.get_id()
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if validator.validate_employee_name:
            self.__name = new_name
        else:
            pass

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if validator.validate_employee_ssn:
            self.__ssn = new_ssn
        else:
            pass

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        if validator.validate_employee_address:
            self.__address = new_address
        else:
            pass

    def get_home_num(self):
        return self.__home_num

    def set_home_num(self, new_home_num):
        if validator.validate_employee_home_num:
            self.__home_num = new_home_num

    def get_mobile_num(self):
        return self.__mobile_num

    def set_mobile_num(self, new_mobile_num):
        if validator.validate_employee_mobile_num:
            self.__mobile_num = new_mobile_num
        else:
            pass

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if validator.validate_employee_email:
            self.__email = new_email
        else:
            pass

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        if validator.validate_employee_title:
            self.__title = new_title
        else:
            pass


class Pilot(Employee):
    def __init__(self, airplane_type=''):
        self.__airplane_type = airplane_type
        pass


class FlightAttendant(Employee):
    def __init__(self):
        pass


class Voyage():
    def __init__(self):
        self.__id = self.get_id()
        self.__destination = self.get_destination()
        self.__airplane = self.get_airplane()
        self.__departure = self.get_flight_departure()
        self.__return = self.get_flight_return()
        self.__pilot = self.get_pilot()
        self.__co_pilot = self.get_pilot()
        self.__purser = self.get_flight_attendant()
        self.__cabin_crew_list = self.get_flight_attendant_list()
        self.__status = ''

    def get_id(self):
        return self.__id

    def get_destination(self):
        return self.__destination

    def get_airplane(self):
        return self.__airplane

    def get_flight_departure(self):
        return self.__departure

    def get_flight_return(self):
        return self.__return

    def get_pilot(self):
        return self.__pilot

    def get_flight_attendant(self):
        return self.__purser

    def get_flight_attendant_list(self):
        return self.__cabin_crew_list

    def generate_flight_number(self):
        return


class Airplane():
    def __init__(self, name='', make='', model='', max_seats=0):
        self.__id = self.get_id()
        self.__name = name
        self.__make = make
        self.__model = model
        self.__max_seats = max_seats

    def get_id(self):
        return


class Destination():
    def __init__(self, country='', airport='', flight_time='', distance='', contact_name='', contact_num=0):
        self.__id = self.get_id()
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_num = contact_num

    def get_id(self):
        return


class Flight():
    def __init__(self, departure_airport='', arrival_airport='',
                 departure_date_time='', arrival_date_time=''):
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_date_time = self.get_departure_date_time()
        self.__arrival_date_time = self.get_arrival_date_time()

        def get_departure_date_time(self):
            return

        def get_arrival_date_time(self):
            return
