from logic_layer.LLAPI import LLAPI
from ui_layer.UIEmployees import UIEmployees
from models.ModelController import ModelController

newUI = UIEmployees(LLAPI(),ModelController())


newUI.display_all_employees()
