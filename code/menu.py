

from datetime import datetime
new_date = datetime.now().replace(microsecond=0).isoformat()
print(new_date)