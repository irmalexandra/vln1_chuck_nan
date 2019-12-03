

class DLAirplanes():
    PLANE_TYPE_ID = 0
    PLANE_NAME = 1
    PLANE_MAKE = 1
    PLANE_MODEL = 2
    MAX_SEATS = 3
    def __init__(self):
        self.all_airplanes_list = []

    def pull_all_airplanes(self):
        
        filestream = open("./repo/Aircraft.csv", "r")
        for line in filestream:
            line_list = line.strip().split(",")



            self.all_airplanes_list.append(line.strip("\n").split(","))
        filestream.closed
        return self.all_airplanes_list[1:]

    def push_all_airplanes(self):
        pass

