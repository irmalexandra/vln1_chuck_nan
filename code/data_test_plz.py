from data_layer.DLAPI import DLAPI




stuff = DLAPI()
emp_list = stuff.populate_all_employees()
for emp in stuff.populate_all_employees():
    print(emp)
for destination in stuff.populate_all_destinations():
    print(destination)

print("------------------------------------")
for airplane in stuff.populate_all_airplanes():
    print(airplane)

stuff.dl_employees.overwrite_all_employees(emp_list)