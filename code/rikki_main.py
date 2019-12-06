from models.AirplaneType import AirplaneType

new_airplane_type = AirplaneType()
new_airplane_type.set_capacity(300)
new_airplane_type.set_make("Boeing")
new_airplane_type.set_model("747")
new_airplane_type.set_plane_type_id()
print(new_airplane_type)
print(new_airplane_type.raw_info())