from validation.validator import Validator


class Employee():

    def __init__(self, name='', ssn='', address='', home_num=0, mobile_num=0, email='', title='', rank='', licence=''):
        self.__models_validation = Validator()
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title
        self.__rank = rank
        self.__licence = licence

        self.__header_format_dict = {"default": self.get_model_header_default_format,
                                     "date": self.get_model_header_date_format,
                                     "aircraft": self.get_model_header_aircraft_format}

        self.__list_info_dict = {"default": self.get_model_list_default_info,
                                 "date": self.get_model_list_date_info,
                                 "aircraft": self.get_model_list_aircraft_info}

<<<<<<< HEAD
        
=======
        self.__validation_dict = {self.get_name: self.set_name, self.get_ssn: self.set_ssn,
                                  self.get_address: self.set_address, self.get_home_num: self.set_home_num,
                                  self.get_mobile_num: self.set_mobile_num, self.get_email: self.set_email}

        self.__creation_order_list = [
            'name', 'ssn', 'home address', 'home number', 'mobile number', 'email']
>>>>>>> f7cfb196b60850d64c7570c2c2d7eb4b7fb83816

    def raw_info(self):
        return self.__ssn + "," + self.__name + "," + str(self.__address) + "," + str(self.__home_num) + "," + str(self.__mobile_num) + "," + self.__email + "," + self.__title + "," + self.__rank + "\n"

    def __str__(self):
        return "Name: {:>2} \nSSN: {:>2} \nAddress: {:>2} \nHome number: {:>2} \nMobile number: {:>2} \nEmail: {:>2} \nTitle: {:>2} \nRank: {:>2}".format(self.__name, self.__ssn, self.__address, self.__home_num, self.__mobile_num, self.__email, self.__title, self.__rank)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__models_validation.validate_employee_name(new_name):
            self.__name = new_name
            return True

        return False

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if self.__models_validation.validate_employee_ssn(new_ssn):
            self.__ssn = new_ssn
            return True

        return False

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        if self.__models_validation.validate_employee_address(new_address):
            self.__address = new_address
            return True

        return False

    def get_home_num(self):
        return self.__home_num

    def set_home_num(self, new_home_num):
        if self.__models_validation.validate_home_number(new_home_num):
            self.__home_num = new_home_num
            return True

        return False

    def get_mobile_num(self):
        return self.__mobile_num

    def set_mobile_num(self, new_mobile_num):
        if self.__models_validation.validate_mobile_number(new_mobile_num):
            self.__mobile_num = new_mobile_num
            return True

        return False

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if self.__models_validation.validate_email(new_email):
            self.__email = new_email
            return True

        return False

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank

    def get_licence(self):
        return self.__licence

    def set_licence(self, new_licence):
        self.__licence = new_licence

    def get_model_header_format(self, header_flag):
        return self.__header_format_dict[header_flag]()

    def get_model_header_date_format(self):
        return "{:20}{:15}{:20}{:20}{:10}".format("Name:",
                                                    "SSN:",
                                                    "Mobile Number:",
                                                    "Title:",
                                                    "Availability:")

    def get_model_header_default_format(self):
        return "{:<10}{:20}{:15}{:20}{:20}{:10}".format("Index: ",
                                                          "Name:",
                                                          "SSN:",
                                                          "Address:",
                                                          "Mobile Number:",
                                                          "Title:")

    def get_model_header_aircraft_format(self):
        return "{:20}{:15}{:20}{:20}{:10}{:10}".format("Name:",
                                                         "SSN:",
                                                         "Address:",
                                                         "Mobile Number:",
                                                         "Title:",
                                                         "Licence:")

    def get_model_list_info(self, header_flag):
        return self.__list_info_dict[header_flag]()

    def get_model_list_date_info(self):
<<<<<<< HEAD
        returnObject = "{:20}{:15}{:20}{:20}{:10}\n".format(
                                                     self.get_name(),
                                                     self.get_ssn(),
                                                     self.get_mobile_num(),
                                                     self.get_title(),
                                                     "Missing availability")
        return returnObject

    def get_model_list_default_info(self):
        returnObject = ("{:20}{:15}{:20}{:20}{:10}\n".format(
                                                                      self.get_name(),
                                                                      self.get_ssn(),
                                                                      self.get_address(),
                                                                      self.get_mobile_num(),
                                                                      self.get_title()))
        return returnObject

    def get_model_list_aircraft_info(self):
        returnObject = "{:20}{:15}{:20}{:20}{:10}{:10}\n".format(
                                                       self.get_name(),
                                                       self.get_ssn(),
                                                       self.get_address(),
                                                       self.get_mobile_num(),
                                                       self.get_title(),
                                                       self.get_licence())
        return returnObject
