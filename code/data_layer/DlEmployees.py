from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot
import os


class DLEmployees():
    ID = 0
    SSN = 1
    NAME = 2
    ADDRESS = 3
    HOME_NUMBER = 4
    MOBILE_NUBER = 5
    EMAIL = 6
    TITLE = 7
    RANK = 8
    LICENSE = 9

    def __init__(self):
        self.all_crew_list = []

    def pull_all_employees(self):
        self.filestream = open("./repo/employees.csv", "r")
        for line in self.filestream:
            line_list = line.strip().split(",")
            if line_list[DLEmployees.TITLE] == 'Pilot':
                new_emp = Pilot()
                new_emp.set_licence(line_list[DLEmployees.LICENSE])
            else:
                new_emp = FlightAttendant()

            new_emp.set_id(line_list[DLEmployees.ID])
            new_emp.set_ssn(line_list[DLEmployees.SSN])
            new_emp.set_name(line_list[DLEmployees.NAME])
            new_emp.set_address(line_list[DLEmployees.ADDRESS])
            new_emp.set_home_num(line_list[DLEmployees.HOME_NUMBER])
            new_emp.set_mobile_num(line_list[DLEmployees.MOBILE_NUBER])
            new_emp.set_email(line_list[DLEmployees.EMAIL])
            new_emp.set_rank(line_list[DLEmployees.RANK])
            new_emp.set_title(line_list[DLEmployees.TITLE])

            self.all_crew_list.append(new_emp)

        return self.all_crew_list

    def overwrite_all_employees(self, emp_list):
        # employee_file.write(new_emp_str)
        HEADER = "id,ssn,name,address,homenumber,mobilenumber,email,role,rank,licence\n"
        filestream2 = open("./repo/employees_temp.csv", "a")
        filestream2.write(HEADER)
        for emp_info in emp_list:
            filestream2.write(emp_info.raw_info())
        filestream2.close()
        os.rename("./repo/employees_temp.csv", "./repo/employees_temp2.csv")
        
        

        
        
    def append_employee(self,employee):
        pass
        
