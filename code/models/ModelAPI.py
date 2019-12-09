from models.Airplane import Airplane
from models.Employee import Employee
from models.Voyage import Voyage
from models.Destination import Destination
from models.AirplaneType import AirplaneType



class ModelAPI():
    def __init__(self):
        self.model_dict = {"Airplane": Airplane,\
                      "Employee": Employee,\
                      "Voyage": Voyage,\
                      "Destination": Destination,
                      "AirplaneType": AirplaneType}


    def get_model(self, model_name):
        model_obj = self.model_dict[model_name]
        return model_obj()

    def get_model_header_format(self, model, header_flag):
        return "|{}|".format(model.get_model_header_format(header_flag))

    def get_model_list_info(self, model_list, header_flag):
        returnObject = ""
        for index, model in enumerate(model_list):
            returnObject += "| {:02d}. {}".format(index+1, model.get_model_list_info(header_flag))
        return returnObject

    def validate_edit_model(self, model):
        ''' Gets a object instance from the logic layer and returns a tuple '''
        validation_dict = model.get_edit_validation_dict()
        edit_order_list = model.get_edit_order_list()
        order_counter = 0

        for key, value in validation_dict.items():
            check = model.handle_key_value(key, value)
            if not check:
                return edit_order_list[order_counter]
            order_counter += 1
        
        return check

    def validate_create_model(self, model):
        ''' Gets a object instance from the logic layer and returns a tuple '''
        validation_dict = model.get_create_validation_dict()
        create_order_list = model.get_create_order_list()
        order_counter = 0

        for key, value in validation_dict.items():
            check = model.handle_key_value(key, value)
            if not check:
                return create_order_list[order_counter]
            order_counter += 1
        
        return check       
