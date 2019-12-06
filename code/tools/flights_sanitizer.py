

FLIGHTNUMBER = 0
DEPARTINGFROM = 1
ARRIVINGAT = 2
DEPARTURE = 3
ARRIVAL = 4
AIRCRAFTID = 5
CAPTAIN = 6
COPILOT = 7
FSM = 8
FA1 = 9
FA2 = 10



flights_stream = open("./old_repo/Flight.csv", "r", encoding="UTF-8")
new_flights_stream = open("./old_repo/newFlights.csv", "a", encoding=("UTF-8"))
employees_stream = open ("./old_repo/employees.csv", "r", encoding="UTF-8")
        

def fix_data():
    old_flights_stream = open("./repo/Flight.csv", "r", encoding="UTF-8")
    new_voyages_stream = open("./repo/voyages.csv", "a", encoding="UTF-8")
    new_voyages_stream.write("departingflightnum,returnflightnum,departingflightdepartingfrom,departingflightdeparturedate,departingflightarrivaldate,returnflightdepartingfrom,returnflightdeparturedate,returnflightarrivaldate,aircraftid,captainid,copilotid,fsmid,faids\n")
    employees_stream = open ("./repo/employees.csv", "r", encoding="UTF-8")
    old_flights_list = []
    employee_list = []
    voyage_list = []
    employee_id_ssn_dict = {}
    
    for flight in flights_stream:
        flight = flight.split(",")
        old_flights_list.append(flight)
    for employee in employees_stream:
        employee = employee.split(",")
        employee_list.append(employee)
    for employee in employee_list:
        employee_id_ssn_dict[employee[1]] = employee[0]
    print()
    for i in range(1,len(old_flights_list)-1,2):
        flight_1 = old_flights_list[i]
        flight_2 = old_flights_list[i+1]
        
        new_voyage = []
        
        departingflightnum = flight_1[FLIGHTNUMBER]
        returnflightnum = flight_2[FLIGHTNUMBER]
        
        departingflightdepartingfrom = flight_1[DEPARTINGFROM]
        departingflightdeparturedate = flight_1[DEPARTURE]
        departingflightarrivaledate = flight_1[ARRIVAL]
        
        returnflightdepartingfrom = flight_2[DEPARTINGFROM]
        returnflightdeparturedate = flight_2[DEPARTURE]
        returnflightarrivaledate = flight_2[ARRIVAL]
        

        try:
            aircraftid = flight_1[AIRCRAFTID]
        except KeyError:
            aircraftid = "."
        try:
            captainid = flight_1[CAPTAIN]
            captainid = employee_id_ssn_dict[captainid]
        except KeyError:
            captainid = "."
        try:
            copilotid = flight_1[COPILOT]
            copilotid = employee_id_ssn_dict[copilotid]
        except KeyError:
            copilotid = "."
        try:
            fsmid = flight_1[FSM]
            fsmid = employee_id_ssn_dict[fsmid]
        except KeyError:
            fsmid = "."
        try:
            fa1id = flight_1[FA1]
            fa1id = employee_id_ssn_dict[fa1id]
        except KeyError:
            fa1id = "."
        try:
            fa2id = flight_1[FA2]
            fa2id = fa2id.strip()
            fa2id = employee_id_ssn_dict[fa2id]
        except KeyError:
            fa2id = "."
        
        faids = []
        faids.append(fa1id)
        faids.append(fa2id)
        faids_str = ":".join(faids)

        new_voyage.append(departingflightnum)
        new_voyage.append(returnflightnum)
        
        new_voyage.append(departingflightdepartingfrom)
        new_voyage.append(departingflightdeparturedate)
        new_voyage.append(departingflightarrivaledate)
        
        new_voyage.append(returnflightdepartingfrom)
        new_voyage.append(returnflightdeparturedate)
        new_voyage.append(returnflightarrivaledate)

        new_voyage.append(aircraftid)
        new_voyage.append(captainid)
        new_voyage.append(copilotid)
        new_voyage.append(fsmid)
        new_voyage.append(faids_str)
        new_voyage_str = ",".join(new_voyage)
        new_voyages_stream.write(new_voyage_str+"\n")


def fix_data2():
    old_flights_stream = open("./old_repo/Flight.csv", "r", encoding="UTF-8")
    new_voyages_stream = open("./voyages.csv", "a", encoding="UTF-8")
    new_voyages_stream.write("departingflightnum,returnflightnum,departingflightdepartingfrom,departingflightdeparturedate,departingflightarrivaldate,returnflightdepartingfrom,returnflightdeparturedate,returnflightarrivaldate,aircraftid,captainid,copilotid,fsmid,faids\n")
    employees_stream = open ("./old_repo/employees.csv", "r", encoding="UTF-8")
    old_flights_list = []
    employee_list = []
    voyage_list = []
    employee_id_ssn_dict = {}
    
    for flight in flights_stream:
        flight = flight.split(",")
        old_flights_list.append(flight)
    for i in range(1,len(old_flights_list)-1,2):
        flight_1 = old_flights_list[i]
        flight_2 = old_flights_list[i+1]
        
        new_voyage = []
        
        departingflightnum = flight_1[FLIGHTNUMBER]
        returnflightnum = flight_2[FLIGHTNUMBER]
        
        departingflightdepartingfrom = flight_1[DEPARTINGFROM]
        departingflightdeparturedate = flight_1[DEPARTURE]
        departingflightarrivaledate = flight_1[ARRIVAL]
        
        returnflightdepartingfrom = flight_2[DEPARTINGFROM]
        returnflightdeparturedate = flight_2[DEPARTURE]
        returnflightarrivaledate = flight_2[ARRIVAL]

        aircraft_id = flight_1[AIRCRAFTID]

        captain_ssn = flight_1[CAPTAIN]
        copilot_ssn = flight_1[COPILOT]

        fsm_ssn = flight_1[FSM]
        fa1 = flight_1[FA1]
        fa2 = flight_1[FA2]
        
        flight_attendants = []
        flight_attendants.append(fa1)
        flight_attendants.append(fa2)
        
        cabin_str = ":".join(flight_attendants)

        new_voyage.append(departingflightnum)
        new_voyage.append(returnflightnum)
        
        new_voyage.append(departingflightdepartingfrom)
        new_voyage.append(departingflightdeparturedate)
        new_voyage.append(departingflightarrivaledate)
        
        new_voyage.append(returnflightdepartingfrom)
        new_voyage.append(returnflightdeparturedate)
        new_voyage.append(returnflightarrivaledate)

        new_voyage.append(aircraft_id)

        new_voyage.append(captain_ssn)
        new_voyage.append(copilot_ssn)
        new_voyage.append(fsm_ssn)

        new_voyage.append(cabin_str)

        new_voyage_str = ",".join(new_voyage)
        new_voyages_stream.write(new_voyage_str)


fix_data2()