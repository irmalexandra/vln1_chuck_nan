from validation.validator import Validator

models_validation = Validator()

class Voyage():
    def __init__(self,departing_flight_num = "",return_flight_num = "",departing_flight_departing_from = "",departing_flight_departure_date = "",departing_flight_arrival_date = "",return_flight_departing_from = "",return_flight_departure_date = "",return_flight_arrival_date = "",aircraft_id = "",captain_id = "",copilot_id = "",fsm_id = "",fa_ids = ""):
        self.departing_flight_num = departing_flight_num
        self.return_flight_num = return_flight_num
        
        self.departing_flight_departing_from = departing_flight_departing_from
        self.departing_flight_departure_date = departing_flight_departure_date
        self.departing_flight_arrival_date = departing_flight_arrival_date
        
        self.return_flight_departing_from = return_flight_departing_from
        self.return_flight_departure_date = return_flight_departure_date
        self.return_flight_arrival_date = return_flight_arrival_date
        
        self.aircraft_id = aircraft_id
        self.captain_id = captain_id
        self.copilot_id = copilot_id
        self.fsm_id = fsm_id
        self.fa_ids = fa_ids
    
    def get_departing_flight_num(self):
        return self.departing_flight_num
    
    def set_departing_flight_num(self, new):
        if models_validation.validate_flight_number(new):
            self.departing_flight_num = new
    
    def get_return_flight_num(self):
        return self.return_flight_num

    def set_return_flight_num(self, new):
        if models_validation.validate_flight_number(new):
            self.return_flight_num = new

    def get_departing_flight_departing_from(self):
        return self.departing_flight_departing_num

    def set_departing_flight_departing_from(self, new):
        if models_validation.validate_city(new):
            self.departing_flight_departing_from = new

    def get_departing_flight_departure_date(self):
        return self.departing_flight_departure_date
    
    def set_departing_flight_departure_date(self, new):
        if models_validation.validate_date_time(new):
            self.departing_flight_departure_date = new

    def get_departing_flight_arrival_date(self):
        return self.departing_arrival_date
    
    def set_departing_flight_arrival_date(self, new):
        if models_validation.validate_date_time(new):
            self.departing_flight_arrival_date = new

    def get_return_flight_departing_from(self):
        return self.return_flight_departing_from

    def set_return_flight_departing_from(self, new):
        if models_validation.validate_city(new):
            self.return_flight_departure_from = new
    
    def get_return_flight_departure_date(self):
        return self.return_flight_departure_date

    def set_return_flight_departure_date(self, new):
        if models_validation.validate_date_time(new):
            self.return_flight_departure_date = new

    def get_return_flight_arrival_date(self):
        return self.return_flight_arrival_date
    
    def set_return_flight_arrival_date(self, new):
        if models_validation.validate_date_time(new):
            self.return_flight_arrival_date = new

    def get_aircraft_id(self):
        return self.aircraft_id
    
    def set_aircraft_id(self, new):
        if models_validation.validate_airplane_id(new):
            self.aircraft_id = new

    def get_captain_id(self):
        return self.captain_id

    def set_captain_id(self, new):
        if models_validation.validate_employee_id(new):
            self.captain_id = new

    def get_copilot_id(self):
        return self.copilot_id
    
    def set_copilot_id(self, new):
        if models_validation.validate_employee_id(new):
            self.copilot_id = new

    def get_fsm_id(self):
        return self.fsm_id
    
    def set_fsm_id(self, new):
        if models_validation.validate_employee_id(new):
            self.fsm_id = new

    def get_fa_ids(self):
        return self.fa_ids

    def set_fa_ids(self, new):
        if models_validation.validate_employee_id(new):
            self.fa_ids.append(new)


