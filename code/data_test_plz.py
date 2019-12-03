from data_layer.DLAPI import DLAPI




stuff = DLAPI()

for emp in stuff.populate_all_employees():
    print(emp)