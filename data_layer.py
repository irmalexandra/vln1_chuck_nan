from models import *

class DLAPI():
    def __init__(self):
        self.dl_employees = DLEmployees()
        self.dl_voyages = DLVoyages()
        self.dl_destinations = DLDestinations()
        self.dl_airplanes = DLAirplanes()

    def populate_all_employees(self):
        return self.dl_employees.pull_all_employees()


    def populate_all_voyages(self):
        return self.dl_voyages.pull_all_voyages()

    def populate_all_destinations(self):
        return self.dl_destinations.pull_all_destinations()

    def populate_all_airplanes(self):
        return self.dl_airplanes.pull_all_airplanes()

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
        self.filestream = open("employees.csv","r")
    def pull_all_employees(self):
        for line in self.filestream:
            line_list = line.strip().split(",")
            if line_list[DLEmployees.TITLE] == 'Pilot':
                new_emp = Pilot()
                new_emp.set_licence(line_list[DLEmployees.LICENSE])
            else:
                new_emp = FlightAttendant()
            new_emp = Employee()
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
        

class DLVoyages():
    def __init__(self):
        pass

    def pull_all_voyages(self):
        all_voyages_list = []
        filestream = open("Flight.csv", "r")
        for line in filestream:
            all_voyages_list.append(line.strip("\n").split(","))
        filestream.closed
        return all_voyages_list[1:]

    def push_all_voyages(self):
        pass


class DLDestinations():
    def __init__(self):
        pass

    def pull_all_destinations(self):
        all_destinations_list = []
        filestream = open("Destination.csv", "r")
        for line in filestream:
            all_destinations_list.append(line.strip("\n").split(","))
        filestream.closed
        return all_destinations_list[1:]

    def push_all_destinations(self):
        pass


class DLAirplanes():
    def __init__(self):
        pass

    def pull_all_airplanes(self):
        all_airplanes_list = []
        filestream = open("Aircraft.csv", "r")
        for line in filestream:
            all_airplanes_list.append(line.strip("\n").split(","))
        filestream.closed
        return all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass


stuff = DLAPI()
# print("What", stuff.populate_all_employees())
# print("\n", stuff.populate_all_airplanes())
# print("\n", stuff.populate_all_destinations())
# print("\n", stuff.populate_all_voyages())
emp_list = stuff.populate_all_employees()
for emp in emp_list:
    print(emp)

