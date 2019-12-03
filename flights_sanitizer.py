FLIGHTNUMBER = 0
DEPARTING = 1
ARRIVING = 2
DEPARTURE = 3
ARRIVAL = 4
AIRCRAFTID = 5
CAPTAIN = 6
COPILOT = 7
FSM = 8
FA1 = 9
FA2 = 10



flights_stream = open("Flight.csv", "r", encoding="UTF-8")
new_flights_stream = open("newFlights.csv", "a", encoding=("UTF-8"))
employees_stream = open ("employees.csv", "r", encoding="UTF-8")


employees_list = []
for line in employees_stream:
    line_list = line.split(",")
    employees_list.append(line_list)


new_flights = []
for index, line in enumerate(flights_stream):
    line_list = line.split(",")
    captain_id = ""
    co_pilot_id = ""
    fsm_id = ""
    fa1_id = ""
    fa2_id = ""
    if index != 0:
        new_ID = ""
        for emp in employees_list:
            fa2_str = line_list[FA2].strip()
            if line_list[CAPTAIN] == emp[1]:
                captain_id = emp[0]
            elif line_list[COPILOT] == emp[1]:
                co_pilot_id = emp[0]
            elif line_list[FSM] == emp[1]:
                fsm_id = emp[0]
            elif line_list[FA1] == emp[1]:
                fa1_id = emp[0]
            elif fa2_str == emp[1]:
                fa2_id = emp[0]
        new_flight = []
        flight_line_list = line.split(",")
        new_flight.append(flight_line_list[FLIGHTNUMBER])
        new_flight.append(flight_line_list[DEPARTING])
        new_flight.append(flight_line_list[ARRIVING])
        new_flight.append(flight_line_list[DEPARTURE])
        new_flight.append(flight_line_list[ARRIVAL])
        new_flight.append(flight_line_list[AIRCRAFTID])
        new_flight.append(captain_id)
        new_flight.append(co_pilot_id)
        new_flight.append(fsm_id)
        try:
            new_flight.append(fa1_id+'='+fa2_id)
        except NameError:
            new_flight.append("-")
        new_flights.append(new_flight)
        

print()
        
        