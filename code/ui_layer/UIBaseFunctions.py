class UIBaseFunctions():
    UI_DIVIDER_INT = 124

    def __init__(self):
        pass

    def back(self):
        return 9
    
    def home(self):
        return 0

    def get_user_input(self, acronym):
        return input("Please enter{}: ".format(acronym))

    def exit_program(self):
        exit()

    def print_object_list(self, object_list, modelAPI, header_flag):
        
        print("-" * self.UI_DIVIDER_INT)
        print(modelAPI.get_model_header_format(object_list[0], header_flag))
        print(modelAPI.get_model_list_info(object_list, header_flag))
        print("-" * self.UI_DIVIDER_INT)

    
        