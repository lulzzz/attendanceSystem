def parse(istream, users):
	data = []
	for isr in istream:
		for usr in users:
			if usr[1] == isr[0]:
				data.append(usr[1])
				data.append(isr[0])
				data.append(isr[1])
				print data
				return data
				break

