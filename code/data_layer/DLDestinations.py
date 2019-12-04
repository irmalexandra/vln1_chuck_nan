from models.ModelController import ModelController


class DLDestinations():
    AIRPORT = 0
    COUNTRY = 1
    FLIGHT_TIME = 2
    DISTANCE = 3
    CONTACT_NAME = 4
    CONTACT_NUMBER = 5

    def __init__(self):
        self.all_destinations_list = []
        self.__model_controller = ModelController()

    def pull_all_destinations(self):

        filestream = open("./repo/Destination.csv", "r")
        for line in filestream:
            line_list = line.strip().split(",")
            new_destination = self.__model_controller.get_model('Destination')

            new_destination.set_airport(line_list[DLDestinations.AIRPORT])
            new_destination.set_country(line_list[DLDestinations.COUNTRY])
            new_destination.set_flight_time(
                line_list[DLDestinations.FLIGHT_TIME])
            new_destination.set_distance(line_list[DLDestinations.DISTANCE])
            new_destination.set_contact_name(
                line_list[DLDestinations.CONTACT_NAME])
            new_destination.set_contact_number(
                line_list[DLDestinations.CONTACT_NUMBER])

            self.all_destinations_list.append(new_destination)
        filestream.closed
        return self.all_destinations_list[1:]

    def push_all_destinations(self):
        pass
