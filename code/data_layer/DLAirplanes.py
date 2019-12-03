

class DLAirplanes():
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

