class LLAirplanes:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.__dl_api.populate_all_airplanes()
