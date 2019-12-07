import os
from os import path


class DLVoyages():
    DEPARTING_FLIGHT_NUM = 0
    RETURNING_FLIGHT_NUM = 1
    DEPARTING_FLIGHT_DEPARTING_FROM = 2
    DEPARTING_FLIGHT_DEPARTING_DATE = 3
    DEPARTING_FLIGHT_ARRIVAL_DATE = 4
    RETURNING_FLIGHT_DEPARTING_FROM = 5
    RETURNING_FLIGHT_DEPARTURE_DATE = 6
    RETURNING_FLIGHT_ARRIVAL_DATE = 7
    airplane_insignia = 8
    CAPTAIN_SSN = 9
    COPILOT_SSN = 10
    FSM_SSN = 11
    FAS_SSN = 12

    def __init__(self, modelAPI):
        self.all_voyages_list = []
        self.__modelAPI = modelAPI

    def pull_all_voyages(self):
        '''Opens csv files and returns a list of all voyages
        (departing flight num, return flight num, departing from, departure date, departing flight arrival date,
        return flight departing from, return flight departure date, return flight arrival date, airplane id, captain ssn,
        copilot ssn, fsm ssn, flight attendants ssn)'''
        if path.exists('./repo/voyages.csv') and path.exists('./repo/voyages_temp.csv'):
            filestream = open("./repo/voyages.csv", "r")
            os.remove("./repo/voyages_temp.csv")
        elif path.exists('./repo/voyages.csv') and path.exists('./repo/voyages_temp.csv') == False:
            filestream = open("./repo/voyages.csv", "r")
        elif path.exists('./repo/voyages.csv') == False and path.exists('./repo/voyages_temp.csv'):
            filestream = open("./repo/voyages_temp.csv", "r")
        else:
            print("Voyage data files not found")
            return

        for line in filestream:
            check_list = []
            line_list = line.strip().split(",")
            new_voyage = self.__modelAPI.get_model('Voyage')
            check_list.append(new_voyage.set_departing_flight_num(
                line_list[DLVoyages.DEPARTING_FLIGHT_NUM]))
            check_list.append(new_voyage.set_return_flight_num(
                line_list[DLVoyages.RETURNING_FLIGHT_NUM]))
            check_list.append(new_voyage.set_departing_flight_departing_from(
                line_list[DLVoyages.DEPARTING_FLIGHT_DEPARTING_FROM]))
            check_list.append(new_voyage.set_departing_flight_departure_date(
                line_list[DLVoyages.DEPARTING_FLIGHT_DEPARTING_DATE]))
            check_list.append(new_voyage.set_departing_flight_arrival_date(
                line_list[DLVoyages.DEPARTING_FLIGHT_ARRIVAL_DATE]))
            check_list.append(new_voyage.set_return_flight_departing_from(
                line_list[DLVoyages.RETURNING_FLIGHT_DEPARTING_FROM]))
            check_list.append(new_voyage.set_return_flight_departure_date(
                line_list[DLVoyages.RETURNING_FLIGHT_DEPARTURE_DATE]))
            check_list.append(new_voyage.set_return_flight_arrival_date(
                line_list[DLVoyages.RETURNING_FLIGHT_ARRIVAL_DATE]))
            check_list.append(new_voyage.set_airplane_insignia(line_list[DLVoyages.airplane_insignia]))
            check_list.append(new_voyage.set_captain_ssn(line_list[DLVoyages.CAPTAIN_SSN]))
            check_list.append(new_voyage.set_copilot_ssn(line_list[DLVoyages.COPILOT_SSN]))
            check_list.append(new_voyage.set_fsm_ssn(line_list[DLVoyages.FSM_SSN]))

            flight_attendant_ssns_list = line_list[DLVoyages.FAS_SSN].split(
                "-")

            check_list.append(new_voyage.set_fa_ssns(flight_attendant_ssns_list))
            if False not in check_list:
                self.all_voyages_list.append(new_voyage)
        filestream.closed
        return self.all_voyages_list[1:]

    def append_voyage(self, new_voyage):
        voyage_stream = open('./repo/voyages.csv', 'a')
        voyage_str = new_voyage.raw_info()
        voyage_stream.write(voyage_str)
        voyage_stream.close()
        return

    def push_all_voyages(self, voyage_list):
        # employee_file.write(new_emp_str)
        HEADER = "departingflightnum,returnflightnum,departingflightdepartingfrom,departingflightdeparturedate,departingflightarrivaldate,returnflightdepartingfrom,returnflightdeparturedate,returnflightarrivaldate,airplanessn,captainssn,copilotssn,fsmssn,fassns\n"
        filestream = open("./repo/voyages_temp.csv", "w")
        filestream.write(HEADER)
        for voyage_info in voyage_list:
            filestream.write(voyage_info.raw_info())
        filestream.close()
        os.remove("./repo/voyages.csv")
        os.rename("./repo/voyages_temp.csv", "./repo/voyages.csv")
        return
