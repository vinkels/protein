import csv

f = open('results/SA_protein_overview/SA_scoreanalyze_16_8_test.csv','r')
data = csv.reader(f, delimiter=',')

row_count = 0
for row in data:
	if row[0] != row[3]:
		print row[0], row[3]
	else:
		print 'same'

	if row_count != 0:
		if int(row[2]) != abs(int(row[4])):
			print row[0], row[2], row[4]
		else:
			print 'same'
	row_count += 1