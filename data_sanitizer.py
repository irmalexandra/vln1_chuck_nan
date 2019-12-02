import random
import string

SSN = 0
NAME = 1
ROLE = 2
RANK = 3
LICENCE = 4


NUMBERS = string.digits
LETTERS = string.ascii_letters
ID = 0


crew_stream = open("crew.csv", "r", encoding="UTF-8")
employee_file = open ("employees.csv", "a", encoding="UTF-8")

def generate_address():
    address = ''
    for i in range(1, random.randint(10,30)):
        address += random.choice(LETTERS)
    return address

def generate_phone_number():
    phone_number = ''
    for i in range(7):
        phone_number += random.choice(NUMBERS)
    return phone_number

def generate_email(name):
    name = name.lower()
    name = name.split()
    name = '.'.join(name)
    return name+"@"+'nanair.is'

sanitized_employees = []
for index,line in enumerate(crew_stream):
    
    new_line = []
    employee = line.split(",")
    if index != 0:
        new_address = generate_address()
        new_home_number = generate_phone_number()
        new_mobile_number = generate_phone_number()
        new_email = generate_email(employee[1])
        ID += 1
        new_id = ID
        new_employee = []
        new_employee.append(str(new_id))
        new_employee.append(str(employee[SSN]))
        new_employee.append(str(employee[NAME]))
        new_employee.append(str(new_address))
        new_employee.append(str(new_home_number))
        new_employee.append(str(new_mobile_number))
        new_employee.append(str(new_email))
        new_employee.append(str(employee[ROLE]))
        new_employee.append(str(employee[RANK]))
        new_employee.append(str(employee[LICENCE]))
        new_emp_str = ','.join(new_employee)
        employee_file.write(new_emp_str)
            

    