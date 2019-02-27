#Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

import sys, csv, tablib

data = tablib.Dataset()

csv_file = open(sys.argv[1], 'r')
csv_reader = csv.reader(csv_file, delimiter=',')

for i in csv_reader:
	data.append(i)

with open(sys.argv[2], 'w') as xls_file:
	xls_file.write(data.xls)

