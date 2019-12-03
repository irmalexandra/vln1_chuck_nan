#from models.Employee import Employee
from ui_layer.UIMain import UIMain
from ui_layer import UIEmployees


def main():
    ui_employee = UIEmployees()
    employee_test = ui_employee.Employee()
    employee_test.set_ssn("2232544444")
    print(employee_test.get_ssn())


main()
