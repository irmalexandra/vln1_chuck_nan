from data_layer.DLAPI import DLAPI
import datetime

stuff = DLAPI()

destination_list = stuff.pull_all_destinations()
for destination in destination_list:
    print(destination)

#stuff.dl_destinations.appent_destination(destination_list[5])

print("------------------------------------ what")
airplane_list = stuff.pull_all_airplanes()
for airplane in airplane_list:
    print(airplane)


#stuff.dl_employees.overwrite_all_employees(emp_list)





the_dict = dict()
the_dict[1] = stuff.pull_all_employees()
idkfam = the_dict[1]
print(the_dict.items())
for item in idkfam:
    print(item)

raw_info = ""
for thing in airplane_list:
    raw_info += (thing.raw_info())
print(raw_info)

#stuff.dl_airplanes.append_airplane(airplane_list[8])

print("------------------------------------------------plz send help")
voyaes = stuff.pull_all_voyages()
for thing in voyaes:
    print(thing)

#stuff.dl_voyages.append_voyage(voyaes[0])

#stuff.dl_voyages.push_all_voyages(voyaes)

print(datetime.datetime(2012,4,2))
print(datetime.date(2012,5,4))

print(datetime.date.today() - datetime.date(2014,5,3))