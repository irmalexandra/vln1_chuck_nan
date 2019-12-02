class LLAPI:
    def __init__(self):
        ll_employees = LLEmployees()
        ll_voyages = LLVoyages()
        ll_destinations = LLDestinations()
        ll_airplanes = LLAirplanes()

class LLEmployees:
    def validate_employee():
        pass

    def get_employee(employee_ID):
        pass

    def get_all_employees():
        pass

    def filter_all_employees_by_date():
        pass

    def filter_all_employees_by_title():
        pass

    def filter_pilots_by_airplane_type():
        pass

    def sort_pilots_bu_airplane_type():
        pass

    def create_work_scedule():
        pass

class LLVoyages:
    def validate_voyage():
        pass

    def get_voyage(voyage_ID):
        pass

    def get_all_voyages():
        pass

    def filter_all_empty_voyages():
        pass

    def filter_all_voyages_by_period():
        pass

    def filter_all_voyages_by_destination():
        pass

    def duplicate_voyages():
        pass

    def repeat_voyage():
        pass

    def add_crew():
        pass
    
class LLDestinations:
    def validate_destination():
        pass

    def get_destination(destination_ID):
        pass

    def get_all_destinations():
        pass
    
class LLAirplanes:
    def validate_airplane():
        pass

    def get_all_airplanes():
        pass
