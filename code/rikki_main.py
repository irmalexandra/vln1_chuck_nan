from models.ModelController import ModelController

model_controller = ModelController()
pilot = model_controller.request_model("Pilot")
pilot.set_ssn("1234567890")
print()

