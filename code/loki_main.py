#from ui_layer.UIEmployees import UIEmployees
from ui_layer import UIEmployees

new_ui_emp = UIEmployees
new_emp = new_ui_emp.Employee()
new_emp.set_ssn("1234567890")
print(new_emp)
