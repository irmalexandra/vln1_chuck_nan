from data_layer.DLAPI import DLAPI




stuff = DLAPI()

for emp in stuff.populate_all_employees():
    print(emp)

for airplane in stuff.populate_all_airplanes():
    print(airplane)