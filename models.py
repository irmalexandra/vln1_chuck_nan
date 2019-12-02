from validation import *

models_validation = Validator()


class Employee():
    def __init__(self, a_id = "", name='', ssn='', address='', home_num=0, mobile_num=0, email='', title='', rank =''):
        self.__id = a_id
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title
        self.__rank = rank


    def __str__(self):
        return "{:<2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(self.__id,self.__name,self.__ssn,self.__address,self.__home_num,self.__mobile_num,self.__email,self.__title,self.__rank)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if models_validation.validate_employee_name:
            self.__name = new_name
        else:
            pass

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if models_validation.validate_employee_ssn:
            self.__ssn = new_ssn
        else:
            pass

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        if models_validation.validate_employee_address:
            self.__address = new_address
        else:
            pass

    def get_home_num(self):
        return self.__home_num

    def set_home_num(self, new_home_num):
        # if models_validation.validate_employee_home_num:
        #     self.__home_num = new_home_num
        self.__home_num = new_home_num
    def get_mobile_num(self):
        return self.__mobile_num

    def set_mobile_num(self, new_mobile_num):
        # if models_validation.validate_employee_mobile_num:
        #     self.__mobile_num = new_mobile_num
        # else:
        #     pass
        self.__mobile_num = new_mobile_num

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        #if models_validation.validate_employee_email:
            #self.__email = new_email
        self.__email = new_email
        # else:
        #     pass

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        # if models_validation.validate_employee_title:
        #     self.__title = new_title
        # else:
        #     pass
        self.__title = new_title

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank




class Pilot(Employee):
    def __init__(self, licence=''):
        super().__init__(self)
        self.__licence = licence

    def get_licence(self):
        return self.__licence

    def set_licence(self, new_licence):
        # if models_validation.validate_pilot_airplane_type:
        #     self.__airplane_type = new_airplane_type
        # else:
        #     pass
        self.__licence = new_licence

    def __str__(self):
        return ( super().__str__(self) + "\n" + self.__licence +"Bitches \n\n")

class FlightAttendant(Employee):
    def __init__(self):
        super().__init__(self)

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

    def set_id(self, new_id):
        if models_validation.validate_voyage_id:
            self.__id = new_id
        else:
            pass

    def get_destination(self):
        return self.__destination

    def set_destination(self, new_destination):
        if models_validation.validate_voyage_destination:
            self.__destination = new_destination
        else:
            pass

    def get_airplane(self):
        return self.__airplane

    def set_airplane(self, new_airplane):
        if models_validation.validate_voyage_airplane:
            self.__airplane = new_airplane
        else:
            pass

    def get_flight_departure(self):
        return self.__departure

    def set_flight_departure(self, new_flight_departure):
        if models_validation.validate_voyage_flight_departure:
            self.__flight_departure = new_flight_departure
        else:
            pass

    def get_flight_return(self):
        return self.__return

    def set_flight_return(self, new_flight_return):
        if models_validation.validate_voyage_flight_return:
            self.__flight_return = new_flight_return
        else:
            pass

    def get_pilot(self):
        return self.__pilot

    def set_pilot(self, new_pilot):
        if models_validation.validate_voyage_pilot:
            self.__pilot = new_pilot
        else:
            pass

    def get_flight_attendant(self):
        return self.__purser

    def set_flight_attendant(self, new_flight_attendant):
        if models_validation.validate_voyage_flight_attendant:
            self.__flight_attendant = new_flight_attendant
        else:
            pass

    def get_flight_attendant_list(self):
        return self.__cabin_crew_list

    def set_flight_attendant_list(self, new_flight_attendant_list):
        if models_validation.validate_voyage_flight_attendant_list:
            self.__flight_attendant_list = new_flight_attendant_list
        else:
            pass

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

    def get_make(self):
        return self.__make

    def set_model(self, new_model):
        if models_validation.validate_airplane_model:
            self.__model = new_model
        else:
            pass

    def get_make(self):
        return self.__make

    def set_max_seats(self, new_max_seats):
        if models_validation.validate_airplane_max_seats:
            self.__max_seats = new_max_seats
        else:
            pass


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
        return self.__id

    def set_id(self, new_id):
        if models_validation.validate_destination_id:
            self.__id = new_id
        else:
            pass

    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        if models_validation.validate_destination_country:
            self.__country = new_country
        else:
            pass

    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        if models_validation.validate_destination_airport:
            self.__airport = new_airport
        else:
            pass

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        if models_validation.validate_destination_flight_time:
            self.__flight_time = new_flight_time
        else:
            pass

    def get_distance(self):
        return self.__distance

    def set_distance(self, new_distance):
        if models_validation.validate_destination_distance:
            self.__distance = new_distance
        else:
            pass

    def get_contact_name(self):
        return self.__contact_name

    def set_contact_name(self, new_contact_name):
        if models_validation.validate_destination_contact_name:
            self.__contact_name = new_contact_name
        else:
            pass

    def get_contact_num(self):
        return self.__contact_num

    def set_contact_num(self, new_contact_num):
        if models_validation.validate_destination_contact_num:
            self.__contact_num = new_contact_num
        else:
            pass


class Flight():
    def __init__(self, departure_airport='', arrival_airport='',
                 departure_date_time='', arrival_date_time=''):
        self.__id = self.get_id()
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_date_time = departure_date_time
        self.__arrival_date_time = arrival_date_time

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if models_validation.validate_flight_id:
            self.__id = new_id
        else:
            pass

    def get_departure_airport(self):
        return self.__departure_airport

    def set_departure_airport(self, new_departure_airport):
        if models_validation.validate_flight_departure_airport:
            self.__departure_airport = new_departure_airport
        else:
            pass

    def get_arrival_airport(self):
        return self.__arrival_airport

    def set_arrival_airport(self, new_arrival_airport):
        if models_validation.validate_flight_arrival_airport:
            self.__arrival_airport = new_arrival_airport
        else:
            pass

    def get_departure_date_time(self):
        return self.__departure_date_time

    def set_departure_date_time(self, new_departure_date_time):
        if models_validation.validate_flight_departure_date_time:
            self.__departure_date_time = new_departure_date_time
        else:
            pass

    def get_arrival_date_time(self):
        return self.__arrival_airport

    def set_arrival_date_time(self, new_arrival_date_time):
        if models_validation.validate_flight_arrival_date_time:
            self.__arrival_date_time = new_arrival_date_time
        else:
            pass
