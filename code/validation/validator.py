class Validator():
    TITLE_LIST = ["Pilot", "Cabincrew"]
    PILOT_RANK_LIST = ["Captain", "Copilot"]
    CABINCREW_RANK_LIST = ["Flight Service Manager", "Flight Attendant"]

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

    def validate_employee_name(self, name):
        return self.validate_name(name)

    def validate_employee_ssn(self, ssn):
        if (self.__validate_int(ssn)) and (len(ssn) == 10):
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
        if (self.__validate_int) and (len(number) == 7):
            return True

        return False

    def validate_mobile_number(self, number):
        return self.validate_phone_number(number)

    def validate_home_number(self, number):
        return self.validate_phone_number(number)

    def validate_email(self, email):
        pass

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

    def validate_airplane_typeid(self, typeid):
        if (self.__validate_string(typeid)) and (typeid.isupper()):
            if typeid[:2] == "NA":
                return True

        return False

    def validate_airplane_name(self, name):
        if name[2] == "-":
            if len(name) == 6:
                return self.__validate_string(name.replace("-", ""))

        return False

    def validate_destinationid(self, id_int):
        if self.__validate_string(id_int):
            if (id_int.isupper()) and (len(id_int) == 3):
                return True

        return False

    def validate_country(self, country):
        return self.__validate_string(country)

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
