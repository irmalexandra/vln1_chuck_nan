class LLAirplanes:
    def __init__(self, DLAPI, model_controller):
        self.__dl_api = DLAPI
        self.__model_controller = model_controller

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.__dl_api.populate_all_airplanes()
