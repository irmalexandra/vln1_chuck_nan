from models.ModelController import ModelController

class DLVoyages():
    DEPARTING_FLIGHT_NUM = 0
    RETURNING_FLIGHT_NUM = 1
    DEPARTING_FLIGHT_DEPARTING_FROM = 2
    DEPARTING_FLIGHT_DEPARTING_DATE = 3
    DEPARTING_FLIGHT_ARRIVAL_DATE = 4
    RETURNING_FLIGHT_DEPARTING_FROM = 5
    RETURNING_FLIGHT_DEPARTURE_DATE = 6
    RETURNING_FLIGHT_ARRIVAL_DATE= 7
    AIRCRAFT_ID = 8
    CAPTAIN_ID = 9
    COPILOT_ID = 10
    FSMID = 11
    FAIDS = 12

    def __init__(self):
        self.all_voyages_list = []
        self.__model_controller = ModelController()

    def pull_all_voyages(self):
        
        filestream = open("./repo/voyages.csv", "r")
        for line in filestream:
            line_list = line.strip().split(",")
            new_voyage = self.__model_controller.get_model('Voyage')
            new_voyage.set_departing_flight_num(line_list[DLVoyages.DEPARTING_FLIGHT_NUM])
            new_voyage.set_return_flight_num(line_list[DLVoyages.RETURNING_FLIGHT_NUM])
            new_voyage.set_departing_flight_departing_from(line_list[DLVoyages.DEPARTING_FLIGHT_DEPARTING_FROM])
            new_voyage.set_departing_flight_departure_date(line_list[DLVoyages.DEPARTING_FLIGHT_DEPARTING_DATE])
            new_voyage.set_departing_flight_arrival_date(line_list[DLVoyages.DEPARTING_FLIGHT_ARRIVAL_DATE])
            new_voyage.set_return_flight_departing_from(line_list[DLVoyages.RETURNING_FLIGHT_DEPARTING_FROM])
            new_voyage.set_return_flight_departure_date(line_list[DLVoyages.RETURNING_FLIGHT_DEPARTURE_DATE])
            new_voyage.set_return_flight_arrival_date(line_list[DLVoyages.RETURNING_FLIGHT_ARRIVAL_DATE])
            new_voyage.set_aircraft_id(line_list[DLVoyages.AIRCRAFT_ID])
            new_voyage.set_captain_id(line_list[DLVoyages.CAPTAIN_ID])
            new_voyage.set_copilot_id(line_list[DLVoyages.COPILOT_ID])
            new_voyage.set_fsm_id(line_list[DLVoyages.FSMID])
            new_voyage.set_fa_ids(line_list[DLVoyages.FAIDS])

        # self.departing_flight_num = departing_flight_num
        # self.return_flight_num = return_flight_num
        
        # self.departing_flight_departing_from = departing_flight_departing_from
        # self.departing_flight_departure_date = departing_flight_departure_date
        # self.departing_flight_arrival_date = departing_flight_arrival_date
        
        # self.return_flight_departing_from = return_flight_departing_from
        # self.return_flight_departure_date = return_flight_departure_date
        # self.return_flight_arrival_date = return_flight_arrival_date
        
        # self.aircraft_id = aircraft_id
        # self.captain_id = captain_id
        # self.copilot_id = copilot_id
        # self.fsm_id = fsm_id
        # self.fa_ids = fa_ids


            self.all_voyages_list.append(new_voyage)
        filestream.closed
        return self.all_voyages_list[1:]

    def push_all_voyages(self):
        pass
