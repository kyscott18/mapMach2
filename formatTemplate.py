import csv

def formatTemplateFile(file):
	"""
	@param file: template file
	@return: array of format for templare data [lat, lon]
	"""
	template = []
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			template.append(row)
	return template