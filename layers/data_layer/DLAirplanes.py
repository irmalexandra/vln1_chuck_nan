from models import *

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
