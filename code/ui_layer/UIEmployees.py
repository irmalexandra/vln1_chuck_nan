from logic_layer.LLAPI import LLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class UIEmployees():
    UI_DIVIDER_INT = 104
    RETURN_MENU_STR = "9. Return 0. Home"
    DEVIATION_INT = 2

    def __init__(self):
        self.ll_api = LLAPI()

    def display_employee_sub_menu(self):
        nav_dict = {1:"",2:self.display_all_employees,3:"",4:"",9:"",0:""}
        employee_menu = "1. Create 2. All 3. Search by"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(employee_menu, " "*(self.UI_DIVIDER_INT -
                                len(employee_menu) - len(self.RETURN_MENU_STR)
                                 - self.DEVIATION_INT), self.RETURN_MENU_STR))

        print("-" * self.UI_DIVIDER_INT)
        while True:
            choice = int(input("Input: "))
            nav_dict[choice]()
            

    def display_employee_search_menu(self):
        ''' Print the search menu of employee sub menu '''
        # needs input
        search_menu = "1. SSN 2. Title 3. Date 4. Airplane"
        print("-" * self.UI_DIVIDER_INT)
        print("|{}{}{}|".format(search_menu, " "*(self.UI_DIVIDER_INT -
                                len(search_menu) - len(self.RETURN_MENU_STR) - 
                                self.DEVIATION_INT), self.RETURN_MENU_STR))

        print("-" * self.UI_DIVIDER_INT)

    def get_employee_by_ssn(self, ssn):
        employee = self.ll_api.get_employee_by_ssn(ssn)
        self.display_employee(employee)

    def display_employee(self, employee):
        pass

    def display_edit_employee(self):
        pass

    def display_all_employees(self):
        ''' Print the given dictionary of employees '''
        print("-" * self.UI_DIVIDER_INT)
        print("|{:<10}{:20}{:15}{:20}{:20}{:10}|".format(
            "Index: ", "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
        employee_dict = self.ll_api.get_all_employee_list()
        for index, employee in employee_dict.items():
            print("|{:02d}{:<8}{:20}{:15}{:20}{:20}{:10}|".format(index,"",
                                                                employee.get_name(),
                                                                employee.get_ssn(),
                                                                employee.get_address(),
                                                                employee.get_mobile_num(),
                                                                employee.get_title()))
        print("-" * self.UI_DIVIDER_INT)

    def display_all_employees_by_date(self):
        '''Displays all employees availability on a specific day'''
        # needs input
        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Mobile Number:", "Title:", "Availability:"))
        employee_list = self.ll_api.get_all_employee_list()
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title(), 
                                                       "Missing availability"))
        print("-" * self.UI_DIVIDER_INT)

    def display_all_employees_by_title(self, title):
        ''' Print a filtered list of all employees by title '''

        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
        employee_list = self.ll_api.get_employee_list_by_title(title)
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_address(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title()))
        print("-" * self.UI_DIVIDER_INT)

    def display_pilots_by_airplane_type_sorted(self):
        ''' print a sorted list of pilots '''

        print("-" * self.UI_DIVIDER_INT)
        print("|{:20}{:15}{:20}{:20}{:10}|".format(
            "Name:", "SSN:", "Address:", "Mobile Number:", "Title:"))
        employee_list = self.ll_api.get_employee_list_by_title("Pilot")
        for employee in employee_list:
            print("|{:20}{:15}{:20}{:20}{:10}|".format(employee.get_name(),
                                                       employee.get_ssn(),
                                                       employee.get_address(),
                                                       employee.get_mobile_num(),
                                                       employee.get_title()))
        print("-" * self.UI_DIVIDER_INT)

    def display_pilots_by_airplane_type_filtered(self, airplane_type):
        pass

    def create_employee(self):
        name = input("Name: ")
        ssn = input("SSN: ")
        home_number = input("Home number: ")
        mobile_number = input("Mobile number: ")
        email = input("E-mail: ")
        title = input("Title: ")
        licence = input("Licence: ")
        availability = input("Availability: ")

    def edit_employee(self):
        pass

    def change_airplane_type(self):
        pass
