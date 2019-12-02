class Validator():

<<<<<<< HEAD
    def __validate_string(self, string):
        if string.isalpha():
            return True
        return False
=======
    def validate_string(name):
        if name.isalpha():
            
            return False
>>>>>>> 8034836696ca619cb70f4274aa93d11353394615

    def __validate_int(self, integer):
        if integer.isdigit():
            return True
        return False

    def validate_employee_name(self, name):
        self.__validate_string(name)

    def validate_employee_ssn(self, ssn):
        self.__validate_int(ssn)

    def validate_employee_address(self, address):

        try:
            name, number = address.split()
            if self.__validate_string(name) and self.__validate_int(number):
                return True

        except ValueError:
            return False
        

def main():
    validation_instance = Validator()
    is_address = validation_instance.validate_employee_address("pulsar 1988")
    print(is_address)

main()

