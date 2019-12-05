from validation.validator import Validator


class Employee():
    def __init__(self, name='', ssn='', address='', home_num=0, mobile_num=0, email='', title='', rank=''):
        self.__models_validation = Validator()
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title
        self.__rank = rank

    def raw_info(self):
        returned_string = ""
        returned_string = str(self.__id) + "," + self.__ssn + "," + self.__name + "," + str(self.__address) + "," + str(
            self.__home_num) + "," + str(self.__mobile_num) + "," + self.__email + "," + self.__title + "," + self.__rank
        return returned_string

    def __str__(self):
        return "Name: {:>2} \nSSN: {:>2} \nAddress: {:>2} \nHome number: {:>2} \nMobile number: {:>2} \nEmail: {:>2} \nTitle: {:>2} \nRank: {:>2}".format(self.__name, self.__ssn, self.__address, self.__home_num, self.__mobile_num, self.__email, self.__title, self.__rank)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__models_validation.validate_employee_name(new_name):
            self.__name = new_name
        else:
            pass

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if self.__models_validation.validate_employee_ssn(new_ssn):
            self.__ssn = new_ssn

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        if self.__models_validation.validate_employee_address(new_address):
            self.__address = new_address
        else:
            pass

    def get_home_num(self):
        return self.__home_num

    def set_home_num(self, new_home_num):
        if self.__models_validation.validate_home_number(new_home_num):
            self.__home_num = new_home_num

    def get_mobile_num(self):
        return self.__mobile_num

    def set_mobile_num(self, new_mobile_num):
        if self.__models_validation.validate_mobile_number(new_mobile_num):
            self.__mobile_num = new_mobile_num
        else:
            pass

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if self.__models_validation.validate_email(new_email):
            self.__email = new_email
        else:
            pass

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        if self.__models_validation.validate_title(new_title):
            self.__title = new_title
        else:
            pass

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank
