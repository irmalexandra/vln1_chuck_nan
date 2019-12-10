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


#stuff.dl_voyages.append_voyage(voyaes[0])

#stuff.dl_voyages.overwrite_all_voyages(voyaes)

#stuff.dl_voyages.overwrite_all_voyages(voyaes)

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
print(range_past <= today <= range_future)

print(date(1,1,1) < date(1,1,2))


print(date(1,1,1) < date(1,1,2))

from logic_layer.LLVoyages import LLVoyages
from models.ModelAPI import ModelAPI
modelAPI = ModelAPI()
voyage = LLVoyages(stuff,modelAPI)  

#print(voyage.calculate_flight_times("2019-12-27T23:40:00","Tingwall"))

voyage.get_all_voyage_list()

other_thing = LLVoyages(stuff,modelAPI)
real_voyages = other_thing.get_all_voyage_list()
print("----------------------------------------------------------------------")
for thing in real_voyages:
    print(thing.get_status())
voyaes = stuff.pull_all_voyages()

#2019-11-18T09:25:00
from logic_layer.LLEmployees import LLEmployees

llemployee = LLEmployees(stuff,ModelAPI)

print(llemployee.get_free_or_not("2019-11-22T10:23:00"))
