from logic_layer.LLAPI import LLAPI
from models import *

LENGTH = 52


class UIAirplanes():
    def __init__(self):
        ll_api = LLAPI()

    def display_airplanes_sub_menu(self):
        print("-" * LENGTH)
        print("{}{}".format("1. Create 2. Display all", "0. Home"))
        print("-" * LENGTH)

    def display_airplanes(self):
        pass

    def create_airplane(self):
        pass
