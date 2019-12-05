<<<<<<< HEAD
from ui_layer.UIMain import UIMain

newui = UImain()

newui.display_main_menu()
=======
from logic_layer.LLAPI import LLAPI
from ui_layer.UIEmployees import UIEmployees
from models.ModelController import ModelController

newUI = UIEmployees(LLAPI(),ModelController())


newUI.display_all_employees()
>>>>>>> 0d8f9d08fbfd60f1df163eb872269949f0f020d5
