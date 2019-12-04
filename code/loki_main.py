from ui_layer.UIEmployees import UIEmployees
#from models.ModelController import ModelController

new_ui_emp = UIEmployees()
new_emp = new_ui_emp.get_employee_instance()
new_emp.set_ssn("1234567890")
new_emp.set_email("hakon.stjani@nanair.is")
print(new_emp)


new_ui_emp.display_all_employees()
