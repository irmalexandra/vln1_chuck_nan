from validation.validator import Validator
class AirplaneType():
    def __init__(self, plane_type_id = "", make = "", model = "", capacity = ""):
        self.__model_validator = Validator()

        self.__plane_type_id = plane_type_id
        self.__make = make
        self.__model = model
        self.__capacity = capacity

        self.__header_format_dict = {"default": self.get_model_header_default_format}

        self.__list_info_dict = {"default": self.get_model_list_default_info}



    def get_model_header_format(self, header_flag):
        return self.__header_format_dict[header_flag]()

    def get_model_list_info(self, header_flag):
        return self.__list_info_dict[header_flag]()
    
    
    def get_model_header_default_format(self):
        return "{:10}{:20}{:17}{:20}{:71}".format("Index:",
                                             "Airplane type:",
                                             "Make:",
                                             "Model:",
                                             "Capacity:")
                                            
        
    def get_model_list_default_info(self):
        returnObject = "     {:20}{:17}{:20}{:71}|\n".format(self.get_plane_type_id(),
                                                              self.get_make(),
                                                              self.get_model(),
                                                              self.get_capacity())
        return returnObject
    
    
    
    def raw_info(self):
        return str(self.__plane_type_id) + "," + str(self.__make) + "," + str(self.__model) + "," + str(self.__capacity)

    def __str__(self):

        return "Airplane type {:>2} \nMake: {:>2} \nModel: {:>2} \nCapacity: {:>2}".format(self.__plane_type_id, self.__make,self.__model,self.__capacity)
    
    def get_plane_type_id(self):
        return self.__plane_type_id

    def set_plane_type_id(self, plane_type_id):
        if self.__model_validator.validate_airplane_typeid(plane_type_id):
            self.__plane_type_id = plane_type_id
            return True
        else:
            return False

    def get_make(self):
        return self.__make

    def set_make(self, make):
        if self.__model_validator.validate_airplane_make(make):
            self.__make = make
            return True
        else:
            return False

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if self.__model_validator.validate_airplane_model(model):
            self.__model = model
            return True
        else:
            return False

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        if self.__model_validator.validate_airplane_capacity(str(capacity)):
            self.__capacity = capacity
            return True
        else:
            return False

