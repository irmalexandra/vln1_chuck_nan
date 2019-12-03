class Validator():
    TITLE_LIST = ["Pilot", "Cabincrew"]
    PILOT_RANK_LIST = ["Captain", "Copilot"]
    CABINCREW_RANK_LIST = ["Flight Service Manager", "Flight Attendant"]
    DOMAIN = "nanair.is"
    PHONE_NUMER = 7
    SSN = 10

    def __validate_string(self, string):
        if string.isalpha():
            return True

        return False

    def __validate_int(self, integer):
        if integer.isdigit():
            return True

        return False

    def validate_name(self, name):
        try:
            first, last = name.split()
            if self.__validate_string(first) and self.__validate_int(last):
                return True

        except ValueError:
            return False

    def validate_employee_id(self, id):
        return self.__validate_int

    def validate_employee_name(self, name):
        return self.validate_name(name)

    def validate_employee_ssn(self, ssn):
        if (self.__validate_int(ssn)) and (len(ssn) == self.SSN):
            return True

        return False

    def validate_employee_address(self, address):
        try:
            name, number = address.split()
            if self.__validate_string(name) and self.__validate_int(number):
                return True

        except ValueError:
            return False

    def validate_phone_number(self, number):
        if (self.__validate_int(number)) and (len(number) == self.PHONE_NUMER):
            return True

        return False

    def validate_mobile_number(self, number):
        return self.validate_phone_number(number)

    def validate_home_number(self, number):
        return self.validate_phone_number(number)

    def validate_email(self, email):
        name, domain = email.split("@")
        if (domain == self.DOMAIN) and ("." in name):
            return True

        return False

    def validate_title(self, title):
        if title in self.TITLE_LIST:
            return True

        return False

    def validate_pilot_rank(self, rank):
        if rank in self.PILOT_RANK_LIST:
            return True

        return False

    def validate_cabincrew_rank(self, rank):
        if rank in self.CABINCREW_RANK_LIST:
            return True

        return False

    def validate_date(self, date):
        if (date[4] == "-") and (date[7] == "-"):
            if len(date) == 10:
                return self.__validate_int(date.replace("-", ""))

        return False

    def validate_time(self, time):
        if (time[2] == ":") and (time[5] == ":"):
            if len(time) == 8:
                return self.__validate_int(time.replace("-", ""))

        return False

    def validate_date_time(self, date_time):
        if (date_time[4] == "-") and (date_time[7] == "-"):
            if (date_time[13] == ":") and (date_time[16] == ":"):
                if len(date_time) == 19:
                    return True

        return False

    def validate_airplane_typeid(self, typeid):
        if (self.__validate_string(typeid)) and (typeid.isupper()):
            if typeid[:2] == "NA":
                return True

        return False

    def validate_airplane_id(self, id):
        if id[2] == "-":
            if len(id) == 6:
                return self.__validate_string(id.replace("-", ""))

        return False

    def validate_airplane_make(self, make):
        return self.__validate_string(make)

    def validate_airplane_model(self, model):
        if model.strip(" ") == model:
            return True
        return False

    def validate_airplane_capacity(self, capacity):
        return self.__validate_int(capacity)

    def validate_destinationid(self, id_int):
        if self.__validate_string(id_int):
            if (id_int.isupper()) and (len(id_int) == 3):
                return True

        return False

    def validate_flight_number(self, flight_num):
        if (self.__validate_string(flight_num[:2])) and (self.__validate_int(flight_num[2:])):
            if (flight_num[:2] == "NA") and (len(flight_num) == 5):
                return True

        return False

    def validate_country(self, country):
        return self.__validate_string(country)

    def validate_city(self, city):
        return self.__validate_string(city)

    def validate_airport(self, airport):
        return self.__validate_string(airport)

    def validate_flight_time(self, time):
        return self.__validate_int(time)

    def validate_distance(self, distance):
        return self.__validate_int(distance)

    def validate_contact_name(self, name):
        return self.validate_name(name)

    def validate_contact_number(self, number):
        return self.validate_phone_number(number)
