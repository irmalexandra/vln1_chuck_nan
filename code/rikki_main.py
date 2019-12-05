from logic_layer.LLAPI import LLAPI
from ui_layer.UIEmployees import UIEmployees
from models.ModelAPI import ModelAPI

newUI = UIEmployees(LLAPI(),ModelAPI())


newUI.display_all_employees()
