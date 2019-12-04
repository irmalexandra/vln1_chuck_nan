from data_layer.DLAPI import DLAPI


stuff = DLAPI()

destination_list = stuff.populate_all_destinations()
for destination in destination_list:
    print(destination)

#stuff.dl_destinations.appent_destination(destination_list[5])

print("------------------------------------ what")
airplane_list = stuff.populate_all_airplanes()
for airplane in airplane_list:
    print(airplane)


#stuff.dl_employees.overwrite_all_employees(emp_list)





the_dict = dict()
the_dict[1] = stuff.populate_all_employees()
idkfam = the_dict[1]
print(the_dict.items())
for item in idkfam:
    print(item)

raw_info = ""
for thing in airplane_list:
    raw_info += (thing.raw_info())
print(raw_info)

#stuff.dl_airplanes.append_aircraft(airplane_list[8])

print("------------------------------------------------plz send help")
voyaes = stuff.populate_all_voyages()
for thing in voyaes:
    print(thing)

#stuff.dl_voyages.append_voyage(voyaes[0])

#stuff.dl_voyages.push_all_voyages(voyaes)