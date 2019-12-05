from logic_layer.LLAPI import LLAPI
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees

new_llapi = LLAPI()
new_modelapi = ModelAPI()
new_uibasefunctions = UIBaseFunctions()


#new_ui_emp = UIEmployees(new_llapi, new_modelapi, new_uibasefunctions)
# new_ui_emp.display_employee_search_menu()
#new_emp = new_ui_emp.get_employee_by_ssn("1811931544")
# new_emp.display_employee(new_emp)
# new_emp.set_ssn("1234567890")
# new_emp.set_email("hakon.stjani@nanair.is")
# print("")
# print(new_emp)


# new_ui_emp.display_all_employees_by_title("Pilot")


all_employee_dict = new_llapi.get_all_employee_dict()
all_employee_list = []
for key, value in all_employee_dict.items():
    all_employee_list.append(value)
all_employee_list.sort(key=lambda employee: employee.get_name(), reverse=False)
#all_employee_dict.sort(key=lambda employee: employee.get_name(), reverse=False)

new_employee_dict = {}

for employee in all_employee_list:
    new_employee_dict[employee.get_id()] = employee

for key, employee in new_employee_dict.items():
    print(employee.get_name())
# for employee in all_employee_list:
    # print(employee.get_name())
