from datetime import datetime, timedelta

from yacka.event import YackaEvent
from yacka.calendar import YackaCalendar
c = YackaCalendar()

#A duration of 15 days, 5 hours and 20 seconds would be:
#P15DT5H0M20S

start_datetime_e1 = "2020-11-01 00:00:00"
end_datetime_e1 = datetime.strptime(start_datetime_e1, '%Y-%m-%d %H:%M:%S')+timedelta(days=0, hours=5, minutes=45)
e1 = YackaEvent(["U1", "U2"], begin=start_datetime_e1, end=end_datetime_e1, name="Hello", description="Description")

c.events.add(e1)

print(c)

c.write("test.ics")
# and it's done !
