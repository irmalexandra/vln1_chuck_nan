from models.ModelController import ModelController
from data_layer.DlEmployees import DLEmployees

dle = DLEmployees()
mdl = ModelController()

new_pilot = mdl.get_model('Pilot')


new_pilot.set_name('Test Pilot')
new_pilot.set_id('39')
new_pilot.set_ssn('1234567890')
new_pilot.set_address('Prufugata 12')
new_pilot.set_home_num('1234567')
new_pilot.set_mobile_num('7654321')
new_pilot.set_email('test.pilot@nanair.is')
new_pilot.set_title('Pilot')
new_pilot.set_rank('Captain')
new_pilot.set_licence('NAFokkerF100')

dle.append_employee(new_pilot)


