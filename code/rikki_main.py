import datetime
now = datetime.datetime.now().replace(microsecond=0).isoformat()


print(now)