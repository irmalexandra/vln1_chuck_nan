from logic_layer.LLAPI import LLAPI

newLLAPI = LLAPI()
all_licences = newLLAPI.get_all_licences()
licence_list = []
    
for airplane in all_licences:
    licence_list.append(airplane.get_plane_type_id())

for licence in licence_list:
    print(licence)