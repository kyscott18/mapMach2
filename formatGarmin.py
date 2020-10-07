import csv

def _dateSpliter(date):
	vec = date.split(',')
	day = vec[0]
	time = vec[1].split()
	n = time[0].split(':')
	secs = (3600 * int(n[0])) + (60 * int(n[1])) + int(n[2])
	if int(n[0]) >= 1 and int(n[0]) < 12 and time[1] == 'PM':
		secs += 60 * 60 * 12
	return day, secs

def _positionSpliter(position):
	loco = position.split()
	lat = float(loco[0][1:3])
	lat += float(loco[1][0:6])/60
	if loco[0][0] == 'S':
		lat *= -1
	lon = float(loco[2][1:3])
	lon += float(loco[3][0:6])/60
	if loco[2][0] == 'W':
		lon *= -1
	return lat, lon

#formats a garmin point to the universal type point
def formatGarminPointToUniversal(row):
	"""
	@param row: the row of the garmin file to be converted
	@return: universal format for incoming data [day, seconds, lat, lon, heading]
	"""
	if row[6] != '':
		day, secs = _dateSpliter(row[1])
		lat, lon = _positionSpliter(row[7])
		heading = row[6].split("°")
		return [day, secs, lat, lon, int(heading[0])]


#format is day, seconds, lat, lon, heading
#formats a garmin file to an array of universal points
def formatGarminFilesToUniversal(files):
	"""
	@param files: an array of the garmin files
	@return: arrays of universal format for incoming data [day, seconds, lat, lon, heading]
	"""
	datas = []
	for file in files:
		data = []
		with open(file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			firstRow = True
			for row in csv_reader:
				if firstRow:
					firstRow = False 
				else:
					data.append(formatGarminPointToUniversal(row))
		datas.append(data)	
	return datas

