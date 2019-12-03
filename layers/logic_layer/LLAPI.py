from data_layer import DLAPI
from models import *


class LLAPI:
    def __init__(self):
        ll_employees = LLEmployees()
        ll_voyages = LLVoyages()
        ll_destinations = LLDestinations()
        ll_airplanes = LLAirplanes()
