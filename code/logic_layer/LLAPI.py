from data_layer import DLAPI
from logic_layer.LLEmployees import LLEmployees
from logic_layer.LLVoyages import LLVoyages
from logic_layer.LLDestinations import LLDestinations
from logic_layer.LLAirplanes import LLAirplanes



class LLAPI:
    def __init__(self):
        ll_employees = LLEmployees()
        ll_voyages = LLVoyages()
        ll_destinations = LLDestinations()
        ll_airplanes = LLAirplanes()
