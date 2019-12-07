class UIBaseFunctions():
    UI_DIVIDER_INT = 124
    DEVIATION_INT = 2
    WALL = "|"

    def __init__(self):
        pass

    def back(self):
        return 9
    
    def home(self):
        return 0

    def get_user_input(self, acronym):
        return input("Please enter {}: ".format(acronym))

    def exit_program(self):
        exit()

    def display_menu(self, menu_str, nav_dict, model = None, return_menu_str = "9. Return 0. Home"):
        while True:
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(menu_str, " "*(self.UI_DIVIDER_INT -len(menu_str) -len(return_menu_str)- self.DEVIATION_INT), return_menu_str))
            print("-" * self.UI_DIVIDER_INT)
            return_bool = int(input("Input: "))
            
            try:

                if model != None:
                    return_bool = nav_dict[return_bool](model)
                else:
                    return_bool = nav_dict[return_bool]()
                if return_bool == 0:
                    return 0
                if return_bool == 9:
                    return
            except KeyError:
                print("Invalid input! try again")
            except TypeError:
                model_index = int(input("Enter index: "))
                model = self.print_model(nav_dict[return_bool][model_index-1])# -1 to account for human readability
                return model

    def display_model_edit_menu(self,menu_str, model, nav_dict, return_menu_str = "9. Return 0. Home"):
        while True:
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(menu_str, " "*(self.UI_DIVIDER_INT -len(menu_str) -len(return_menu_str)- self.DEVIATION_INT), return_menu_str))
            print("-" * self.UI_DIVIDER_INT)
            return_bool = int(input("Input: "))
            edit_dict = model.get_edit_dict()
            try:
                return_bool = nav_dict[return_bool]()
                if return_bool == 0:
                    return 0
                if return_bool == 9:
                    return
                
            except KeyError:
                print("Invalid input")
            except TypeError:
                attribute_key = nav_dict[return_bool]
                changed_attribute_str = self.get_user_input(attribute_key)
                edit_dict[attribute_key](changed_attribute_str)
                self.print_model(model)
                return 
            


    def print_model_list(self, model_list, modelAPI, header_flag):
        
        print("-" * self.UI_DIVIDER_INT)
        print(modelAPI.get_model_header_format(model_list[0], header_flag))
        print(modelAPI.get_model_list_info(model_list, header_flag))
        print("-" * self.UI_DIVIDER_INT)
        return
    
    def print_model(self, model):
        print("-" * self.UI_DIVIDER_INT)
        print(model)
        print("-" * self.UI_DIVIDER_INT)
        return model

    
    