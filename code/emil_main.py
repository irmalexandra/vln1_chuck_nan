from data_layer.DLAPI import DLAPI


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

#stuff.dl_voyages.push_all_voyages(voyaes)

from datetime import date

work_year = 2018
work_day = 5
work_month = 3
work = date(work_year,work_month,work_day)
employee = ["Derpster","Pilot","Divorced", work]
print("---------------------------------")
for info in employee:
    print(info)
print("----------------------------------")
today = date.today()
tomorrow = date(2019,12,8)

print(today - date(2014,5,3))


print(date.today())

print(tomorrow - today)
print("Date from:")
#range_high = date(int(input("Year: ")),int(input("Month: ")),int(input("Day: ")))
range_past= date(2019,12,1)
print("Date to:")
range_future = date(2019,12, 11)

print(range_future >= today >= range_past)


print(date(1,1,1) < date(1,1,2))


print(date(1,1,1) < date(1,1,2))

