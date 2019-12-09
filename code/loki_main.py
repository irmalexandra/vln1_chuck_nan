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

voyage_list = new_llapi.get_all_voyage_list()

voyage = voyage_list[32]

