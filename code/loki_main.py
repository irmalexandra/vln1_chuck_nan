from models.Employee import Employee
#from ui_layer.UIMain import UIMain


def main():
    #uimain = UIMain()
    #uimain.
    employee_test = Employee()
    employee_test.set_ssn("2232544444")
    print(employee_test.get_ssn())


main()
