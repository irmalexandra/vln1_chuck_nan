class LLDestinations:
    DESTINATION_EDIT_CONTACT_NAME_FLAG = 0
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_destinations = []

    def validate_destination(self):
        pass

    def edit_destination(self, destination, input_tpl):
        if input_tpl[self.DESTINATION_EDIT_CONTACT_NAME_FLAG] == 0:
            success_check = destination.set_contact_name(input_tpl)
            self.__dl_api.overwrite_all_destinations(self.__all_destinations)
            return success_check
        else:
            return destination.set_contact_number(input_tpl)

    def get_one_destination(self, airport):
        self.__all_destinations = self.get_all_destinations()

        for destination in all_destinations:
            if destination.get_airport() == airport:
                return destination

    def get_all_destinations(self):
        return self.__dl_api.populate_all_destinations()

    def push_all_destinations(self):
        self.__dl_api.overwrite_all_destinations()
