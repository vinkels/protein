import csv

f = open('results/final/SA_percentageanalyze_14_7.csv','r')
data = csv.reader(f, delimiter=',')

out = open('results/final/SA_percentageanalyze_14_7_without.csv','w')
csv_file = csv.writer(out, delimiter = ',')

for row in data:
	if row != '':
		csv_file.writerow(row)