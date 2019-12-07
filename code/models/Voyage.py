from validation.validator import Validator


class Voyage():
    def __init__(self, destination = "", departing_flight_num = "", return_flight_num = "", departing_flight_departing_from = "", 
                departing_flight_departure_date = "", departing_flight_arrival_date = "", return_flight_departing_from = "", 
                return_flight_departure_date = "", return_flight_arrival_date = "", airplane_insignia = "", 
                captain_ssn = "", copilot_ssn = "", fsm_ssn = "", fa_ssns=[]):
        self.__models_validation = Validator()
        self.__departing_flight_num = departing_flight_num
        self.__return_flight_num = return_flight_num

        self.__destination = destination

        self.__departing_flight_departing_from = departing_flight_departing_from
        self.__departing_flight_departure_date = departing_flight_departure_date
        self.__departing_flight_arrival_date = departing_flight_arrival_date

        self.__return_flight_departing_from = return_flight_departing_from
        self.__return_flight_departure_date = return_flight_departure_date
        self.__return_flight_arrival_date = return_flight_arrival_date

        self.__airplane_ssn = airplane_insignia
        self.__captain_ssn = captain_ssn
        self.__copilot_ssn = copilot_ssn
        self.__fsm_ssn = fsm_ssn
        self.__fa_ssns = fa_ssns

        self.__validation_dict = {self.get_destination:self.set_destination, 
                                self.get_departing_flight_departure_date:self.set_departing_flight_departure_date}

        self.__creation_order_list = ["destination", "departure date"]

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.__departing_flight_num, self.__return_flight_num, self.__departing_flight_departing_from, self.__departing_flight_departure_date, self.__departing_flight_arrival_date, self.__return_flight_departing_from, self.__return_flight_departure_date, self.__return_flight_arrival_date, self.__airplane_insignia, self.__captain_ssn, self.__copilot_ssn, self.__fsm_ssn, ":".join(self.__fa_ssns))

    def raw_info(self):
        true_employees = ":".join(self.__fa_ssns)
        return self.__departing_flight_num + "," + self.__return_flight_num + "," + self.__departing_flight_departing_from + "," + self.__departing_flight_departure_date + "," + self.__departing_flight_arrival_date + "," + self.__return_flight_departing_from + "," + self.__return_flight_departure_date + "," + self.__return_flight_arrival_date + "," + self.__airplane_insignia + "," + self.__captain_ssn + "," + self.__copilot_ssn + "," + self.__fsm_ssn + "," + true_employees + "\n"

    def get_validation_dict(self):
        return self.__validation_dict

    def get_creation_order_list(self):
        return self.__creation_order_list

    def handle_key_value(self, key, value):
        return value(key())

    def get_destination(self):
        return self.__destination
    
    def set_destination(self, airport):
        if self.__models_validation.validate_airport(airport):
            self.__destination = airport
            return True
        return False

    def get_departing_flight_num(self):
        return self.__departing_flight_num

    def set_departing_flight_num(self, new):
        if self.__models_validation.validate_flight_number(new):
            self.__departing_flight_num = new

    def get_return_flight_num(self):
        return self.__return_flight_num

    def set_return_flight_num(self, new):
        if self.__models_validation.validate_flight_number(new):
            self.__return_flight_num = new

    def get_departing_flight_departing_from(self):
        return self.__departing_flight_departing_from

    def set_departing_flight_departing_from(self, new):
        if self.__models_validation.validate_city(new):
            self.__departing_flight_departing_from = new
        self.__departing_flight_departing_from = new

    def get_departing_flight_departure_date(self):
        return self.__departing_flight_departure_date

    def set_departing_flight_departure_date(self, new_departure):
        if self.__models_validation.validate_date_time(new_departure):
            self.__departing_flight_departure_date = new_departure

    def get_departing_flight_arrival_date(self):
        return self.__departing_flight_arrival_date

    def set_departing_flight_arrival_date(self, new):
        if self.__models_validation.validate_date_time(new):
            self.__departing_flight_arrival_date = new

    def get_return_flight_departing_from(self):
        return self.__return_flight_departing_from

    def set_return_flight_departing_from(self, new):
        if self.__models_validation.validate_city(new):
            self.__return_flight_departing_from = new
        self.__return_flight_departing_from = new

    def get_return_flight_departure_date(self):
        return self.__return_flight_departure_date

    def set_return_flight_departure_date(self, new):
        if self.__models_validation.validate_date_time(new):
            self.__return_flight_departure_date = new

    def get_return_flight_arrival_date(self):
        return self.__return_flight_arrival_date

    def set_return_flight_arrival_date(self, new):
        if self.__models_validation.validate_date_time(new):
            self.__return_flight_arrival_date = new

    def get_airplane_insignia(self):
        return self.__airplane_insignia

    def set_airplane_insignia(self, new):
        if new != ".":
            if self.__models_validation.validate_airplane_insignia(new):
                self.__airplane_insignia = new
        else:
            self.__airplane_insignia = new

    def get_captain_ssn(self):
        return self.__captain_ssn

    def set_captain_ssn(self, new):
        if new != ".":
            if self.__models_validation.validate_employee_ssn(new):
                self.__captain_ssn = new
        else:
            self.__captain_ssn = new

    def get_copilot_ssn(self):
        return self.__copilot_ssn

    def set_copilot_ssn(self, new):
        if new != ".":
            if self.__models_validation.validate_employee_ssn(new):
                self.__copilot_ssn = new
        else:
            self.__copilot_ssn = new

    def get_fsm_ssn(self):
        return self.__fsm_ssn

    def set_fsm_ssn(self, new):
        if new != ".":
            if self.__models_validation.validate_employee_ssn(new):
                self.__fsm_ssn = new
        else:
            self.__fsm_ssn = new

    def get_fa_ssns(self):
        return self.__fa_ssns

    def set_fa_ssns(self, new):
        if new != ".":
            valid_ssns = []
            for emp_ssn in new:
                if self.__models_validation.validate_employee_ssn(emp_ssn):
                    valid_ssns.append(emp_ssn)
            self.__fa_ssns = valid_ssns
