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


        self.__header_format_dict = {"default": self.get_model_header_default_format}

        self.__list_info_dict = {"default": self.get_model_list_default_info}

        self.__create_validation_dict = {self.get_destination: self.set_destination, 
                                         self.get_departing_flight_departure_date: self.set_departing_flight_departure_date}

        self.__create_order_list = ["destination", "departure date"]

        self.__voyage_employee_ssn_dict = {"Captain":self.get_captain_ssn, 
                                           "Copilot":self.get_copilot_ssn, 
                                           "Flight Service Manager":self.get_fsm_ssn, 
                                           "Flight Attendant":self.get_fa_ssns}

    def __str__(self):
        return "{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}".format(self.__departing_flight_num, self.__return_flight_num, self.__departing_flight_departing_from, self.__departing_flight_departure_date, self.__departing_flight_arrival_date, self.__return_flight_departing_from, self.__return_flight_departure_date, self.__return_flight_arrival_date, self.__airplane_insignia, self.__captain_ssn, self.__copilot_ssn, self.__fsm_ssn, ":".join(self.__fa_ssns))

    def raw_info(self):
        true_employees = ":".join(self.__fa_ssns)
        return self.__departing_flight_num + "," + self.__return_flight_num + "," + self.__departing_flight_departing_from + "," + self.__departing_flight_departure_date + "," + self.__departing_flight_arrival_date + "," + self.__return_flight_departing_from + "," + self.__return_flight_departure_date + "," + self.__return_flight_arrival_date + "," + self.__airplane_insignia + "," + self.__captain_ssn + "," + self.__copilot_ssn + "," + self.__fsm_ssn + "," + true_employees + "\n"

    def get_create_validation_dict(self):
        return self.__create_validation_dict

    def get_create_order_list(self):
        return self.__create_order_list

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

    def set_departing_flight_num(self, flight_number):
        if self.__models_validation.validate_flight_number(flight_number):
            self.__departing_flight_num = flight_number

    def get_return_flight_num(self):
        return self.__return_flight_num

    def set_return_flight_num(self, flight_number):
        if self.__models_validation.validate_flight_number(flight_number):
            self.__return_flight_num = flight_number       

    def get_flight_times(self):
        pass

    def set_flight_times(self, departing_flight_arrival_date, return_flight_departure_date, return_flight_arrival_date):
        self.set_departing_flight_arrival_date(departing_flight_arrival_date)
        self.set_return_flight_departure_date(return_flight_departure_date)
        self.set_return_flight_arrival_date(return_flight_arrival_date)
        pass

    def get_departing_flight_departing_from(self):
        return self.__departing_flight_departing_from

    def set_departing_flight_departing_from(self, flight_number):
        if self.__models_validation.validate_name(flight_number):
            self.__departing_flight_departing_from = flight_number
        

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
        if self.__models_validation.validate_name(new):
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

    def get_voyage_employee_ssn(self, rank):
        return self.__voyage_employee_ssn_dict[rank]()

    
    def get_model_header_format(self, header_flag):
        return self.__header_format_dict[header_flag]()

    def get_model_list_info(self, header_flag):
        return self.__list_info_dict[header_flag]()

    def change_date_time_format(self, date_string):
        date_string = date_string[:-3].replace("T", " ")
        return date_string

    def get_model_header_default_format(self):
        return "{:7}{:15}{:11}{:20}{:20}{:16}{:16}{:10}{:7}".format("Index:",
                                                            "Destination:",
                                                            "Airplane:",
                                                            "Dep date/time:",
                                                            "Ret date/time:",
                                                            "Dep flight no:",
                                                            "Ret flight no:",
                                                            "Staffed:", 
                                                            "Status:")

    def get_model_list_default_info(self):
        return "  {:15}{:11}{:20}{:20}{:16}{:16}{:10}{:7}|\n".format(self.get_return_flight_departing_from(),
                                                                   self.get_airplane_insignia(),  # we should change this to airplane type
                                                                   self.change_date_time_format(self.get_departing_flight_departure_date()),
                                                                   self.change_date_time_format(self.get_return_flight_arrival_date()),
                                                                   self.get_departing_flight_num(),
                                                                   self.get_return_flight_num(),
                                                                   "staffed",
                                                                   "status")
            