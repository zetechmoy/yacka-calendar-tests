
from yacka.calendar import YackaCalendar
from datetime import timedelta

c = YackaCalendar.read("yackalendar.ics")

print(c)
print("#########################################")
c.add_event("2020-11-01 00:00:00", timedelta(days=0, hours=0, minutes=30), "Trajet", "Ceci est un super trajet !", ["U1", "U2"])
print(c)

c.write("yackalendar.ics")
