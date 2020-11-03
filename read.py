from yacka.calendar import YackaCalendar

c = YackaCalendar(imports=open("yackalendar.ics", "r").read())

#print(c.events)
print(c)
