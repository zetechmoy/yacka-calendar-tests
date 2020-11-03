from ics import Calendar
from yacka.event import YackaEvent
from yacka.utils import basic_parse
from datetime import datetime
import os

class YackaCalendar(Calendar):
	"""docstring for YackaCalendar."""

	def __init__(self, imports=None):
		self.imports = imports
		super(YackaCalendar, self).__init__(imports=imports)

		#convert event to yacka event
		if self.imports != None:
			new_events = list()
			for event in self.events:
				ye = self.event_to_yackaevent(event)
				new_events.append(ye)

			self.events = set(new_events)

	def event_to_yackaevent(self, event):
		parsed_event = basic_parse(event.__str__())

		nb_users = parsed_event.get("NBUSERS", None)
		uids = list()

		if nb_users != None:
			for i in range(0, int(nb_users)):
				uids.append(parsed_event.get("USER"+str(i), None))
		else:
			raise Exception(event + "\n is not a YackaEvent")

		ye = YackaEvent(uids, begin=event.begin, end=event.end, name=event.name, description=event.description)
		return ye

	def write(self, filename):
		with open(filename, 'w') as f:
			f.writelines(self)

	def add_event(self, start_datetime, timed, title, description, users):
		#start_datetime => format "2020-11-01 00:00:00"
		#users => list of strings (for ids) ["u1", "u2"]
		end_datetime = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')+timed
		e1 = YackaEvent(users, begin=start_datetime, end=end_datetime, name=title, description=description)
		self.events.add(e1)

	@staticmethod
	def read(filename):
		if os.path.exists(filename):
			return YackaCalendar(imports=open(filename, "r").read())
		else:
			return YackaCalendar()
