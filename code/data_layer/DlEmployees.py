from models.Employee import Employee
from models.Employee import Pilot
from models.Employee import FlightAttendant

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
        self.filestream = open("./repo/employees.csv","r")
    def pull_all_employees(self):
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
        
        return self.all_crew_list[1:]

    def push_all_employees(self, emp_list):
        #employee_file.write(new_emp_str)
        header = self.all_crew_list[0]
        raw_output = ""
        for line in emp_list:
            for thing in line:
                raw_output += str(thing) +","
        #print(raw_output)
        filestream2 = open("Crew2.csv","w")
        filestream2.write("lol")
        
        