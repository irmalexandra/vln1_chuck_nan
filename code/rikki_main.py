<<<<<<< HEAD
import datetime
now = datetime.datetime.now().replace(microsecond=0).isoformat()


print(now)
=======
from models.ModelController import ModelController
from logic_layer.LLAPI import LLAPI

def menu():
    while True:
        print("menu")
        i = int(input("Enter: "))
        a = nav_dict[i]()
        if a == "0":
            return "0"
        if a == "9":
            return

def subMenu():
    while True:
        print("subMenu")
        i = int(input("Enter: "))
        a = nav_dict[i]()
        if a == "0":
            return "0"
        if a == "9":
            return

def subSubMenu():
    while True:
        print("subSubMenu")
        i = int(input("Enter: "))
        a = nav_dict[i]()
        if a == "0":
            return "0"
        if a == "9":
            return 
        

def back():
    return "9"

def home():
    return "0"

nav_dict = {1: menu, 2: subMenu, 3:subSubMenu, 9:back, 0:home}

def run():
    while True:
        stackCount = 1
        i = int(input("Enter: "))
        nav_dict[i]()

run()
>>>>>>> 762dc04e5066bdf32b86eca304ec34d664925356
