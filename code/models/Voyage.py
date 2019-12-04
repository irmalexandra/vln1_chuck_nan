from validation.validator import Validator

models_validation = Validator()


class Voyage():
    def __init__(self, departing_flight_num="", return_flight_num="", departing_flight_departing_from="", departing_flight_departure_date="", departing_flight_arrival_date="", return_flight_departing_from="", return_flight_departure_date="", return_flight_arrival_date="", aircraft_id="", captain_id="", copilot_id="", fsm_id="", fa_ids=[]):
        self.__departing_flight_num = departing_flight_num
        self.__return_flight_num = return_flight_num

        self.__departing_flight_departing_from = departing_flight_departing_from
        self.__departing_flight_departure_date = departing_flight_departure_date
        self.__departing_flight_arrival_date = departing_flight_arrival_date

        self.__return_flight_departing_from = return_flight_departing_from
        self.__return_flight_departure_date = return_flight_departure_date
        self.__return_flight_arrival_date = return_flight_arrival_date

        self.__aircraft_id = aircraft_id
        self.__captain_id = captain_id
        self.__copilot_id = copilot_id
        self.__fsm_id = fsm_id
        self.__fa_ids = fa_ids

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.__departing_flight_num , self.__return_flight_num , self.__departing_flight_departing_from  , self.__departing_flight_departure_date  , self.__departing_flight_arrival_date , self.__return_flight_departing_from , self.__return_flight_departure_date , self.__return_flight_arrival_date  , self.__aircraft_id , self.__captain_id, self.__copilot_id , self.__fsm_id ,":".join(self.__fa_ids))

    def raw_info(self):
        true_employees =":".join(self.__fa_ids)
        return self.__departing_flight_num + "," + self.__return_flight_num + "," + self.__departing_flight_departing_from + "," + self.__departing_flight_departure_date + "," + self.__departing_flight_arrival_date + "," + self.__return_flight_departing_from + "," + self.__return_flight_departure_date + "," + self.__return_flight_arrival_date + "," + self.__aircraft_id + "," + self.__captain_id + "," + self.__copilot_id + "," + self.__fsm_id + "," + true_employees + "\n"

    def get_departing_flight_num(self):
        return self.__departing_flight_num

    def set_departing_flight_num(self, new):
        if models_validation.validate_flight_number(new):
            self.__departing_flight_num = new

    def get_return_flight_num(self):
        return self.__return_flight_num

    def set_return_flight_num(self, new):
        if models_validation.validate_flight_number(new):
            self.__return_flight_num = new

    def get_departing_flight_departing_from(self):
        return self.__departing_flight_departing_from

    def set_departing_flight_departing_from(self, new):
        if models_validation.validate_city(new):
            self.__departing_flight_departing_from = new
        self.__departing_flight_departing_from = new

    def get_departing_flight_departure_date(self):
        return self.__departing_flight_departure_date

    def set_departing_flight_departure_date(self, new):
        if models_validation.validate_date_time(new):
            self.__departing_flight_departure_date = new

    def get_departing_flight_arrival_date(self):
        return self.__departing_flight_arrival_date

    def set_departing_flight_arrival_date(self, new):
        if models_validation.validate_date_time(new):
            self.__departing_flight_arrival_date = new

    def get_return_flight_departing_from(self):
        return self.__return_flight_departing_from

    def set_return_flight_departing_from(self, new):
        if models_validation.validate_city(new):
            self.__return_flight_departing_from = new
        self.__return_flight_departing_from = new

    def get_return_flight_departure_date(self):
        return self.__return_flight_departure_date

    def set_return_flight_departure_date(self, new):
        if models_validation.validate_date_time(new):
            self.__return_flight_departure_date = new

    def get_return_flight_arrival_date(self):
        return self.__return_flight_arrival_date

    def set_return_flight_arrival_date(self, new):
        if models_validation.validate_date_time(new):
            self.__return_flight_arrival_date = new

    def get_aircraft_id(self):
        return self.__aircraft_id

    def set_aircraft_id(self, new):
        if new != ".":
            if models_validation.validate_airplane_id(new):
                self.__aircraft_id = new
        else:
            self.__aircraft_id = new

    def get_captain_id(self):
        return self.__captain_id

    def set_captain_id(self, new):
        if new != ".":
            if models_validation.validate_employee_id(new):
                self.__captain_id = new
        else:
            self.__captain_id = new

    def get_copilot_id(self):
        return self.__copilot_id

    def set_copilot_id(self, new):
        if new != ".":
            if models_validation.validate_employee_id(new):
                self.__copilot_id = new
        else:
            self.__copilot_id = new

    def get_fsm_id(self):
        return self.__fsm_id

    def set_fsm_id(self, new):
        if new != ".":
            if models_validation.validate_employee_id(new):
                self.__fsm_id = new
        else:
            self.__fsm_id = new

    def get_fa_ids(self):
        return self.__fa_ids

    def set_fa_ids(self, new):
        if new != ".":
            valid_ids = []
            for emp_id in new:
                if models_validation.validate_employee_id(emp_id):
                    valid_ids.append(emp_id)
            self.__fa_ids = valid_ids
