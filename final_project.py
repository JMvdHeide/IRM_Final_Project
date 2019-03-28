#!/usr/bin/env python3
# Jarik van der Heide
# s2964007

# Code for processing raw data for the final project of Introduction to Research Methods

from collections import defaultdict

def readfile():
	"""Reads the raw data and converts it to a more usable format"""
	reports = []
	with open('aangifte-politie_buurten.csv', 'r') as csv:
		for line in csv:
			line = line.rstrip().split(';')
			line2 = []
			for element in line:
				if element == '' or element == '-':
					line2.append(0)
				else:
					line2.append(element)
			reports.append(line2)
	
	return reports

def process(reports):
	"""Takes the usable fomat and processes it to form a new csv file with the needed data"""
	with open('police_reports_Groningen.csv', 'a+') as new_csv:
		new_csv.write("district;police_reports\n")
		districts = defaultdict(int)
		for line in reports[2:]:
			total_reports = 0
			for i in [5, 9, 13, 17, 21, 25, 29]:
				total_reports += int(line[i])
			districts[line[0][:-2]] += total_reports

		for k, v in districts.items():
			new_csv.write(str(k) + ";" + str(v) + '\n')

def main():
	reports = readfile()
	process(reports)

if __name__ == '__main__':
	main()