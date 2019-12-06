from data_layer.DLAPI import DLAPI

new_DLAPI = DLAPI()

airplane_list = new_DLAPI.populate_all_airplanes()
for airplane in airplane_list:
    print(airplane)
