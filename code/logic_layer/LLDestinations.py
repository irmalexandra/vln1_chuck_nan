class LLDestinations:
    DESTINATION_EDIT_CONTACT_NAME_FLAG = 0
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_destination_list = []

    def create_destination(self, destination):
        if self.validate_destination(destination):
            self.__dl_api.append_destination(destination)
            return True
            
        return False

    def validate_destination(self, destination):
        ''' Gets destination instance and returns a boolean '''
        return self.__modelAPI.validate_model(destination)

    def get_all_destination_list(self):
        ''' Gets a list of destination instances and returns it '''
        self.__all_destination_list = self.__dl_api.pull_all_destinations()
        return self.__all_destination_list

    def overwrite_all_destinations(self):
        ''' Takes a list of destination instances and sends it to the DL ''' 
        return self.__dl_api.overwrite_all_destinations(self.__all_destination_list)

    def get_destination_list_by_country(self, country):
        ''' Gets input from UI layer and returns an instance '''

        self.__all_destination_list = self.get_all_destination_list()
        found_destination_list = []

        for destination in self.__all_destination_list:
            if destination.get_country() == country:
                found_destination_list.append(destination)
        
        return found_destination_list

