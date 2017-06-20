import csv

f = open('results/SA_protein_overview/SA_percentageanalyze_16_8.csv','r')
data = csv.reader(f, delimiter=',')

out = open('results/final/SA_percentageanalyze_16_8.csv','w')
csv_file = csv.writer(out, delimiter = ',')

for row in data:
	if row != '':
		csv_file.writerow(row)