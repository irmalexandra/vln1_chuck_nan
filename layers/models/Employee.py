from validation import *

models_validation = Validator()


class Employee():
    def __init__(self, a_id = "", name='', ssn='', address='', home_num=0, mobile_num=0, email='', title='', rank =''):
        self.__id = a_id
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__home_num = home_num
        self.__mobile_num = mobile_num
        self.__email = email
        self.__title = title
        self.__rank = rank


    def __str__(self):
        return "{:<2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(self.__id,self.__name,self.__ssn,self.__address,self.__home_num,self.__mobile_num,self.__email,self.__title,self.__rank)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if models_validation.validate_employee_name:
            self.__name = new_name
        else:
            pass

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if models_validation.validate_employee_ssn:
            self.__ssn = new_ssn
        else:
            pass

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        if models_validation.validate_employee_address:
            self.__address = new_address
        else:
            pass

    def get_home_num(self):
        return self.__home_num

    def set_home_num(self, new_home_num):
        # if models_validation.validate_employee_home_num:
        #     self.__home_num = new_home_num
        self.__home_num = new_home_num
    def get_mobile_num(self):
        return self.__mobile_num

    def set_mobile_num(self, new_mobile_num):
        # if models_validation.validate_employee_mobile_num:
        #     self.__mobile_num = new_mobile_num
        # else:
        #     pass
        self.__mobile_num = new_mobile_num

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        #if models_validation.validate_employee_email:
            #self.__email = new_email
        self.__email = new_email
        # else:
        #     pass

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        # if models_validation.validate_employee_title:
        #     self.__title = new_title
        # else:
        #     pass
        self.__title = new_title

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank

