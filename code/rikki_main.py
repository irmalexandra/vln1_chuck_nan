from models.ModelController import ModelController
from data_layer.DLAPI import DLAPI

dlapi = DLAPI()

airplanes = dlapi.populate_all_airplanes()
destinations = dlapi.populate_all_destinations()
voyage = dlapi.populate_all_voyages()
empl = dlapi.populate_all_employees()

print(airplanes)
print(destinations)
print(voyage)
print(empl)