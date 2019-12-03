from models.Employee import Employee


def main():
    employee_test = Employee()
    employee_test.set_ssn("22325444444")
    print(employee_test.get_ssn())


main()
