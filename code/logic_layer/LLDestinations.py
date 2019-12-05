class LLDestinations:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_destination(self):
        pass

    def edit_destination(self, destination, input_tpl):
        if input_tpl[0] == 0:
            return destination.set_contact_name(input_tpl)
        else:
            return destination.set_contact_number(input_tpl)

    def get_one_destination(self, airport):
        all_destinations = self.get_all_destinations()

        for destination in all_destinations:
            if destination.get_airport() == airport:
                return destination

    def get_all_destinations(self):
        return self.__dl_api.populate_all_destinations()

    def push_all_destinations(self):
        self.__dl_api.overwrite_all_destinations(destination_list)
