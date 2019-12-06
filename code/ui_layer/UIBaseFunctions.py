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

    def display_menu(self, menu_str, nav_dict, return_menu_str = "9. Return 0. Home"):
        while True:
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(menu_str, " "*(self.UI_DIVIDER_INT -len(menu_str) -len(return_menu_str)- self.DEVIATION_INT), return_menu_str))
            print("-" * self.UI_DIVIDER_INT)
            return_bool = int(input("Input: "))
            try:
                return_bool = nav_dict[return_bool]()
                if return_bool == 0:
                    return 0
                if return_bool == 9:
                    return
                if return_bool == 1:
                    object_index = int(input("Enter index: "))
                    self.print_object(nav_dict[return_bool][object_index])
                    return
            except KeyError:
                print("Invalid input! try again")
            except TypeError:
                object_index = int(input("Enter index: "))
                self.print_object(nav_dict[return_bool][object_index-1])# -1 to account for human readability
                return


    def print_object_list(self, object_list, modelAPI, header_flag):
        
        print("-" * self.UI_DIVIDER_INT)
        print(modelAPI.get_model_header_format(object_list[0], header_flag))
        print(modelAPI.get_model_list_info(object_list, header_flag))
        print("-" * self.UI_DIVIDER_INT)
        return
    
    def print_object(self, object):
        print("-" * self.UI_DIVIDER_INT)
        print(object)
        print("-" * self.UI_DIVIDER_INT)

    
    