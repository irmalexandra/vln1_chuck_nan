class UIAirplanes():
    RETURN_MENU_STR = "9. Return 0. Home"


    def __init__(self, LLAPI, modelAPI, UIBaseFunctions):
        self.__ll_api = LLAPI
        self.__modelAPI = modelAPI
        self.__ui_base_functions = UIBaseFunctions

    def get_airplanes_sub_menu(self):
            nav_dict = {1:self.create_airplane,
                        2:self.get_all_airplanes,
                        3:self.get_airplane_search_menu,
                        9:self.__ui_base_functions.back,
                        0:self.__ui_base_functions.home}
            airplane_menu = "1. Create 2. Get all 3. Search by"
            return_value = self.__ui_base_functions.print_menu(airplane_menu,nav_dict)
            return self.__ui_base_functions.check_return_value(return_value)
    
    def get_airplane_search_menu(self):
        nav_dict = {1: self.get_all_airplanes_by_date,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        airplane_menu = "1. Date"
        return_value = self.__ui_base_functions.print_menu(airplane_menu,nav_dict)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_airplane_type_list_menu(self, airplane_type_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        employee_menu = "1. Select airplane type"
        return_value = self.__ui_base_functions.print_menu(employee_menu, nav_dict, airplane_type_list)
        return self.__ui_base_functions.check_return_value(return_value)
        
    def create_airplane(self):
        new_airplane = self.__modelAPI.get_model("Airplane")
        airplane_type_list = self.__ll_api.get_airplane_type_list()
        existing_airplane_types_list = self.__ll_api.get_airplane_type_list()
        header_flag = "default"
        return_value = self.__ui_base_functions.print_model_list(airplane_type_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_type_list_menu(return_value)
        if return_value != None and return_value != 0:
            make = return_value.get_make()
            model = return_value.get_model()
            airplane_type_id = return_value.get_plane_type_id()
            new_airplane.set_make(make)
            new_airplane.set_model(model)
            while True:
                insignia = self.__ui_base_functions.get_user_input("Insignia (must be 3 letters): TF-")
                check = new_airplane.set_insignia("TF-" +insignia)
                if check:
                    if self.__ll_api.create_airplane(new_airplane, existing_airplane_types_list,insignia):
                        print("\nAirplane created!\n{}".format(new_airplane))
                        return
                    else:
                        print("\n{}\nAlready exists!".format(new_airplane.get_insignia()))
                else:
                    print("\nInvalid insignia {}\n".format(insignia))
        return self.__ui_base_functions.check_return_value(return_value)

    def get_select_from_airplane_list_menu(self,airplanes_list):
        nav_dict = {1: self.__ui_base_functions.select_from_model_list,
                    9: self.__ui_base_functions.back,
                    0: self.__ui_base_functions.home}
        airplane_menu = "1. Select airplane"
        return_value = self.__ui_base_functions.print_menu(airplane_menu,nav_dict,airplanes_list)
        return self.__ui_base_functions.check_return_value(return_value)
    
    def get_all_airplanes(self):
        header_flag = "default"
        airplanes_list = self.__ll_api.get_all_airplane_list()
        return_value = self.__ui_base_functions.print_model_list(airplanes_list,self.__modelAPI,header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_list_menu(airplanes_list)
        return self.__ui_base_functions.check_return_value(return_value)

    def get_all_airplanes_by_date(self):
        new_date = self.__ui_base_functions.get_user_date_input("date", "DD-MM-YYYY")
        new_time = self.__ui_base_functions.get_user_date_input("time", "HH:MM")
        header_flag = "default"
        airplane_list = self.__ll_api.get_all_airplane_list_by_period(new_date, new_time)
        return_value = self.__ui_base_functions.print_model_list(
            airplane_list, self.__modelAPI, header_flag)
        if type(return_value).__name__ == "list":
            return_value = self.get_select_from_airplane_list_menu(airplane_list)
        return self.__ui_base_functions.check_return_value(return_value)