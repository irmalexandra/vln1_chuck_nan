from logic_layer.LLAPI import LLAPI
from logic_layer.LLVoyages import LLVoyages
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees
from datetime import datetime
new_llapi = LLAPI()
new_modelapi = ModelAPI()
new_uibasefunctions = UIBaseFunctions()

new_ll_voyages = LLVoyages

employee_list = new_llapi.get_all_employee_list()

new_emp = employee_list[1]

voyage_list = new_llapi.get_all_voyage_list()

voyage = voyage_list[32]

avail_list = new_ll_voyages.filter_available_employees(new_ll_voyages,"Captain", voyage)

print(avail_list)
