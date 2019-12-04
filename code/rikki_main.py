from models.ModelController import ModelController
from data_layer.DlEmployees import DLEmployees

dle = DLEmployees()

emp_list = dle.pull_all_employees()
spec_emp = emp_list[-1]
spec_emp.set_name('Rikki Frikk')
dle.overwrite_all_employees(emp_list)