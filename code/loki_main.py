from ui_layer.UIEmployees import UIEmployees
#from models.ModelController import ModelController

new_ui_emp = UIEmployees()
new_ui_emp.display_employee_search_menu()
new_emp = new_ui_emp.get_employee_by_ssn("1811931544")
new_emp.set_ssn("1234567890")
new_emp.set_email("hakon.stjani@nanair.is")
print("")
print(new_emp)


#new_ui_emp.display_all_employees_by_title("Pilot")
