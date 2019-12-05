from validation.validator import Validator


class Voyage():
    def __init__(self, departing_flight_num="", return_flight_num="", departing_flight_departing_from="", departing_flight_departure_date="", departing_flight_arrival_date="", return_flight_departing_from="", return_flight_departure_date="", return_flight_arrival_date="", aircraft_id="", captain_ssn="", copilot_ssn="", fsm_ssn="", fa_ssns=[]):
        self.__models_validation = Validator()
        self.__departing_flight_num = departing_flight_num
        self.__return_flight_num = return_flight_num

        self.__departing_flight_departing_from = departing_flight_departing_from
        self.__departing_flight_departure_date = departing_flight_departure_date
        self.__departing_flight_arrival_date = departing_flight_arrival_date

        self.__return_flight_departing_from = return_flight_departing_from
        self.__return_flight_departure_date = return_flight_departure_date
        self.__return_flight_arrival_date = return_flight_arrival_date

        self.__aircraft_ssn = aircraft_ssn
        self.__captain_ssn = captain_ssn
        self.__copilot_ssn = copilot_ssn
        self.__fsm_ssn = fsm_ssn
        self.__fa_ssns = fa_ssns

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.__departing_flight_num, self.__return_flight_num, self.__departing_flight_departing_from, self.__departing_flight_departure_date, self.__departing_flight_arrival_date, self.__return_flight_departing_from, self.__return_flight_departure_date, self.__return_flight_arrival_date, self.__aircraft_id, self.__captain_ssn, self.__copilot_ssn, self.__fsm_ssn, ":".join(self.__fa_ssns))

    def raw_info(self):
        true_employees = ":".join(self.__fa_ssns)
        return self.__departing_flight_num + "," + self.__return_flight_num + "," + self.__departing_flight_departing_from + "," + self.__departing_flight_departure_date + "," + self.__departing_flight_arrival_date + "," + self.__return_flight_departing_from + "," + self.__return_flight_departure_date + "," + self.__return_flight_arrival_date + "," + self.__aircraft_id + "," + self.__captain_ssn + "," + self.__copilot_ssn + "," + self.__fsm_ssn + "," + true_employees + "\n"

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

    def set_departing_flight_departure_date(self, new):
        if self.__models_validation.validate_date_time(new):
            self.__departing_flight_departure_date = new

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

    def get_aircraft_id(self):
        return self.__aircraft_id

    def set_aircraft_id(self, new):
        if new != ".":
            if self.__models_validation.validate_airplane_id(new):
                self.__aircraft_id = new
        else:
            self.__aircraft_id = new

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
