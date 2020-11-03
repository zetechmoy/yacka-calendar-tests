from ics import Calendar, Event
from datetime import timedelta

class YackaEvent(Event):

	def __init__(self, uids, begin=None, duration=None, end=None, name=None, description=None):
		self.uids = uids
		super(YackaEvent, self).__init__(begin=begin, duration=duration, end=end, name=name, description=description)

	def __str__(self):
		orig_ics = super().__str__()
		orig_ics_lines = orig_ics.split("\r\n")
		i = 0
		while i < len(orig_ics_lines):
			if orig_ics_lines[i].startswith("NBUSERS"):
				del orig_ics_lines[i]
			elif orig_ics_lines[i].startswith("USER"):
				del orig_ics_lines[i]
			elif orig_ics_lines[i].startswith("RRULE"):
				del orig_ics_lines[i]
			else:
				i += 1

		yacka_ics_lines = list()

		#adding users to ics
		yacka_ics_lines.append("NBUSERS:"+str(len(self.uids)))

		for i in range(0, len(self.uids)):
			yacka_ics_lines.append("USER"+str(i)+":"+self.uids[i])

		#adding weekly support of trips
		yacka_ics_lines.append("RRULE:FREQ=WEEKLY")

		#insert yacka lines
		last_line = orig_ics_lines[len(orig_ics_lines)-1]
		del orig_ics_lines[len(orig_ics_lines)-1]
		orig_ics_lines.extend(yacka_ics_lines)
		orig_ics_lines.append(last_line)

		return '\r\n'.join(orig_ics_lines)

	def __repr__(self):
		return super().__repr__().replace("Event", "YackaEvent")
