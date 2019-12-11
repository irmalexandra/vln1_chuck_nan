from datetime import datetime
def get_user_date_input(date_or_time, date_or_time_format):
    while True:
        
        new_date_or_time = input("Please enter {} ({}): ".format(date_or_time ,date_or_time_format))
        try:
            if date_or_time_format == "DD-MM-YYYY":
                datetime.strptime(new_date_or_time,'%d-%m-%Y')
                return new_date_or_time

            if date_or_time_format == "HH:MM":
                datetime.strptime(new_date_or_time,'%H:%M')
                new_date_or_time += ":00"
                return new_date_or_time
        except ValueError:
            print("Invalid date format for ({})!".format(date_or_time_format))
        


print(get_user_date_input("date","DD-MM-YYYY"))
print(get_user_date_input("time","HH:MM"))