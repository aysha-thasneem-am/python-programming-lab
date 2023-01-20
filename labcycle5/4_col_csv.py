import csv
with open("test.csv","r") as file:
	cs = csv.DictReader(file)
	for row in cs:
		print(row['brand'])
