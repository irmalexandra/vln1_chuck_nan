# from ui_layer.UIAirplanes import UIAirplanes
# new_ui_des = UIAirplanes()


# new_ui_des.display_airplanes_sub_menu()
# new_ui_des.create_airplane()
# new_ui_des.display_all_airplanes()


# from ui_layer.UIDestinations import UIDestinations
# new_ui_des = UIDestinations()


# new_ui_des.display_destination_sub_menu()
# new_ui_des.create_destination()
# new_ui_des.display_all_destinations()
# new_ui_des.destination_search_menu()
# new_ui_des.destination_search_sub_menu()

# from logic_layer.LLEmployees import LLEmployees
# new_ll_emp = LLEmployees()

# new_ll_emp.filter_all_employees_by_title()


# from ui_layer.UIVoyages import UIVoyages
# new_ui_des = UIVoyages()

# new_ui_des.display_voyage_sub_menu()

# # new_ui_des.create_voyage()
# # new_ui_des.display_all_voyages()
# # new_ui_des.display_one_voyage()
# # new_ui_des.voyages_search_menu()
# # new_ui_des.voyages_search_sub_menu()
# new_ui_des.voyages_search_sub_sub_menu()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from logic_layer.LLAPI import LLAPI
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees

new_llapi = LLAPI()
new_modelapi = ModelAPI()
new_uibasefunctions = UIBaseFunctions()

new_ui_des = UIEmployees(new_llapi, new_modelapi, new_uibasefunctions)
# new_ui_des.display_employee_search_menu()
new_ui_des.display_employee_sub_menu()
new_ui_des.get_employee_by_ssn('3009907461')
# new_ui_des.get_employee_by_ssn('3009907461')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# from data_layer.DLAPI import DLAPI
# from models.ModelAPI import ModelAPI
# from logic_layer.LLEmployees import LLEmployees

# new_dlapi = DLAPI()
# new_modelapi = ModelAPI()

# new_ui_des = LLEmployees(new_dlapi, new_modelapi)
# new_ui_des.get_employee_by_ssn(3009907461)
