from logic_layer.LLAPI import LLAPI
from logic_layer.LLVoyages import LLVoyages
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees
from datetime import datetime
new_llapi = LLAPI()

new_uibasefunctions = UIBaseFunctions()

employee_list = new_llapi.get_all_employee_list()

new_emp = employee_list[1]

voyage_list = new_llapi.get_all_voyage_list()

voyage = voyage_list[32]

airplanes = new_llapi.get_all_available_airplane_list(voyage)

print(airplanes)

avail_list = new_llapi.get_filtered_employee_list_for_voyage("Captain", voyage)#new_llapi.get_all_empty_voyage_list()

print(avail_list)
