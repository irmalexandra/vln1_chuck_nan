import os
from os import path

class DLDestinations():
    COUNTRY = 0
    AIRPORT = 1
    FLIGHT_TIME = 2
    DISTANCE = 3
    CONTACT_NAME = 4
    CONTACT_NUMBER = 5

    def __init__(self, modelAPI):
        self.all_destinations_list = []
        self.__modelAPI = modelAPI

    def pull_all_destinations(self):

        if path.exists('./repo/destination.csv') and path.exists('./repo/destinations_temp.csv'):
            filestream = open("./repo/destination.csv", "r")
            os.remove("./repo/destinations_temp.csv")
        elif  path.exists('./repo/destination.csv') and path.exists('./repo/destinations_temp.csv') == False:
            filestream = open("./repo/destination.csv", "r")
        elif path.exists('./repo/destination.csv') == False and path.exists('./repo/destinations_temp.csv'):
            filestream = open("./repo/destinations_temp.csv", "r")
        else:
            print("destination data files not found")
            return

        for line in filestream:
            line_list = line.strip().split(",")
            new_destination = self.__modelAPI.get_model('Destination')

            new_destination.set_country(line_list[DLDestinations.COUNTRY])
            new_destination.set_airport(line_list[DLDestinations.AIRPORT])
            new_destination.set_flight_time(line_list[DLDestinations.FLIGHT_TIME])
            new_destination.set_distance(line_list[DLDestinations.DISTANCE])
            new_destination.set_contact_name(line_list[DLDestinations.CONTACT_NAME])
            new_destination.set_contact_number(line_list[DLDestinations.CONTACT_NUMBER])

            self.all_destinations_list.append(new_destination)
        filestream.closed
        return self.all_destinations_list[1:]

    def appent_destination(self, new_destination):
        destination_stream = open('./repo/Destination.csv', 'a')
        destination_str = new_destination.raw_info()
        destination_stream.write(destination_str)
        destination_stream.close()
        return    


    def push_all_destinations(self, destination_list):
        # employee_file.write(new_emp_str)
        HEADER = "country,airport,flight time,distance,contact name,contact number\n"
        filestream = open("./repo/destinations_temp.csv", "w")
        filestream.write(HEADER)
        for destination_info in destination_list:
            filestream.write(destination_info.raw_info())
        filestream.close()
        os.remove("./repo/destination.csv")
        os.rename("./repo/destinations_temp.csv", "./repo/destination.csv")
        return