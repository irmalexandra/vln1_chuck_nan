class LLVoyages:
    def __init__(self, DLAPI, model_controller):
        self.__dl_api = DLAPI
        self.__model_controller = model_controller

    def validate_voyage(self):
        pass

    def get_voyage(self, voyage_ID):
        pass

    def get_all_voyages(self):
        return self.__dl_api.populate_all_voyages()

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
