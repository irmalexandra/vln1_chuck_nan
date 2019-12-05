from data_layer.DLAPI import DLAPI

new_DLAPI = DLAPI()

for plane in new_DLAPI.populate_all_airplanes():
    print(plane)

for destination in new_DLAPI.populate_all_destinations():
    print(destination)

for voyage in new_DLAPI.populate_all_voyages():
    print(voyage)

for emp in new_DLAPI.populate_all_employees():
    print(emp)

