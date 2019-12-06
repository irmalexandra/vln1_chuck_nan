from data_layer.DLAPI import DLAPI

new_DLAPI = DLAPI()

airplane_list = new_DLAPI.pull_all_airplanes()
for airplane in airplane_list:
    print(airplane)
