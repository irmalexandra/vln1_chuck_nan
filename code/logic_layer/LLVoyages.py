class LLVoyages:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_voyage(self):
        pass

    def get_voyage(self, voyage_ID):
        pass

    def get_all_voyages(self):
        return self.__dl_api.pull_all_voyages()

    def filter_all_empty_voyages(self):
        pass

    def filter_all_voyages_by_period(self):
        pass

    def filter_all_voyages_by_destination(self):
        pass

    def duplicate_voyages(self):
        pass

    def repeat_voyage(self):
        pass

    def add_crew(self):
        pass
