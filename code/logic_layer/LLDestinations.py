class LLDestinations:
    DESTINATION_EDIT_CONTACT_NAME_FLAG = 0
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_destinations = []

    def validate_destination(self):
        pass

    def edit_destination(self, destination, input_tpl):
        set_contact_info_dict = {0: destination.set_contact_name, 1: destination.set_contact_number}
        success_check = set_contact_info_dict[input_tpl[0]](input_tpl[1])
        if success_check:
            self.__dl_api.overwrite_all_destinations(self.__all_destinations)
        return success_check

    def get_one_destination(self, airport):
        self.__all_destinations = self.get_all_destinations()

        for destination in self.__all_destinations:
            if destination.get_airport() == airport:
                return destination

    def get_all_destinations(self):
        return self.__dl_api.populate_all_destinations()

    def push_all_destinations(self):
        self.__dl_api.overwrite_all_destinations()
