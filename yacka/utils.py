

def basic_parse(ics_format_string):
	ics_lines = ics_format_string.split("\r\n")
	d = dict()
	for ics_line in ics_lines:
		k, v = ics_line.split(":")
		d[k] = v

	return d
