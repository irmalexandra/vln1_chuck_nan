import datetime
class Validator():
    TITLE_LIST = ["Pilot", "Cabin Crew"]
    PILOT_RANK_LIST = ["Captain", "Copilot"]
    CABINCREW_RANK_LIST = ["Flight Service Manager", "Flight Attendant"]
    DOMAIN = "nanair.is"
    PHONE_NUMBER = 7
    SSN = 10

    def __validate_string(self, attribute):
        attribute = str(attribute)
        return attribute.isalpha()

    def __validate_int(self, attribute):
        try:
            int(attribute)
            return True
        except ValueError:
            return False

    def validate_name(self, name):
        try:
            name = name.replace(" ", "")
            if self.__validate_string(name):
                return True

        except ValueError:
            return False

    def validate_employee_name(self, name):
        return self.validate_name(name)

    def validate_employee_ssn(self, ssn):
        try:
            if ssn[6] == '-':
                ssn = ssn.replace("-", "")
            if (self.__validate_int(ssn)) and (len(ssn) == self.SSN):
                return True
        except IndexError:
            return False

        return False

    def validate_employee_address(self, address):
        try:
            name, number = address.split()
            if self.__validate_string(name) and self.__validate_int(number):
                return True

        except ValueError:
            return False

    def validate_phone_number(self, number):
        if (self.__validate_int(number)) and (len(number) == self.PHONE_NUMBER):
            return True

        return False

    # gera rad fyrir landnumeri (+354)?
    def validate_mobile_number(self, number):
        return self.validate_phone_number(number)

    def validate_home_number(self, number):
        return self.validate_phone_number(number)

    def validate_email(self, email): # <---- Useless?
        try:
            name, domain = email.split("@")
            if (domain == self.DOMAIN) and ("." in name):
                return True
        except ValueError:
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

    def validate_date(self, date_str):
        try:
            year, month, day = date_str.split("-")
            datetime.date(int(year),int(month),int(day))
            return True
        except ValueError:
            return False


    def validate_time(self, time_str):
        try:
            hour, minute, second = time_str.split(":")
            datetime.time(int(hour),int(minute),int(second))
            return True
        except ValueError:
            return False

    def validate_date_time(self, date_time):
        try:
            date, time = date_time.split("T")
        except ValueError:
            return False
        return self.validate_date(date) and self.validate_time(time)


    def validate_airplane_typeid(self, typeid):
        return typeid[:2] == "NA"

    def validate_airplane_insignia(self, insignia):
        if insignia[2] == "-":
            if len(insignia) == 6:
                return self.__validate_string(insignia.replace("-", ""))

        return False

    def validate_airplane_make(self, make):
        return self.__validate_string(make)

    def validate_airplane_model(self, model):
        if model.strip() == model:
            return True
        return False

    def validate_airplane_capacity(self, capacity):
        return self.__validate_int(capacity)

    def validate_flight_number(self, flight_num):
        if (flight_num[:2] == "NA") and (self.__validate_int(flight_num[2:])):
            return True

        return False

    def validate_country(self, country):
        return self.validate_name(country)

    def validate_airport(self, airport):
        return self.validate_name(airport)

    def validate_flight_time(self, time):
        return self.__validate_int(time)

    def validate_distance(self, distance):
        return self.__validate_int(distance)

    def validate_contact_name(self, name):
        return self.validate_name(name)

    def validate_contact_number(self, number):
        return self.validate_phone_number(number)