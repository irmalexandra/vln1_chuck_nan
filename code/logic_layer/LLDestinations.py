class LLDestinations:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_destination(self):
        pass

    def get_destination(self, destination_ID):
        pass

    def get_all_destinations(self):
        return self.__dl_api.populate_all_destinations()
