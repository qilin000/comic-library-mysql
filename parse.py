import csv

class CSV():
	"""Parses a raw CSV file to an array"""
	
	def __init__(self, filename=None):
		self.file = filename

	def read_file(self):
		with open(self.file, 'r') as f:
			data = [row for row in csv.reader(f.read().splitlines())]
		return data

	def get_row_count(self):
		return len(self.read_file())

	def get_column_count(self):
		temp_file = self.read_file()
		return len(temp_file[0])

	def get_data(self, start=0,end=1):
		data = self.read_file()
		return data[start:end]

	# add method to parse csv to json