from logic_layer.LLAPI import LLAPI
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees
from datetime import datetime
new_llapi = LLAPI()
new_modelapi = ModelAPI()
new_uibasefunctions = UIBaseFunctions()

employee_list = new_llapi.get_all_employee_list()

new_emp = employee_list[1]

work_schedule = new_llapi.get_work_schedule_list(new_emp)

date = "08-12-2019"
time = "23:59:33"

#day, month, year = date.split("-")
#hour, minute, second = time.split(":")

#iso_date = datetime(year, month, day)
#iso_time = datetime.time(hour, minute, second)



#print(new_emp)
#for voyage in work_schedule:
    #print(voyage)



#new_ui_emp = UIEmployees(new_llapi, new_modelapi, new_uibasefunctions)
#a_destination = new_llapi.get_one_destination("Reykjavik")
#destination_success = new_modelapi.validate_model(a_destination)
#print(destination_success)
# new_emp.set_ssn("1234567890")
# new_emp.set_email("hakon.stjani@nanair.is")
# print("")
# print(new_emp)


# new_ui_emp.display_all_employees()
def get_iso_format_date_time(date='', time=''):

    if time != "":
        time = datetime.strptime(time,'%H:%M:%S').time()
    if date != "":
        date = datetime.strptime(date,'%d-%m-%Y').date()

    return date, time

datetime_date = get_iso_format_date_time("02-02-2002")

print(datetime_date)

date = datetime(2019,11,24,10,37,00)

print(type(date).__name__)