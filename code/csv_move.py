import shutil
import os.path
import fnmatch
import csv
from pathlib import Path


protein_array = []
csv_name = 'analyze2_50_30_500'
f = open('results/final/%s.csv' % (csv_name),'r')
data = csv.reader(f, delimiter=',')

source = '/Users/yannick/Desktop/code/minor_programming/protein/code/results'
dest1 = '/Users/yannick/Desktop/code/minor_programming/protein/code/results/SA_50_2_15'


for row in data:
	if row[0] != 'protein':
		protein_array.append(row[0])
		print row[0]
# print protein_array

files = os.listdir(source)
# print files

 
for i in range(14):
	for protein in protein_array:
		# print protein
		my_file = 'result_anneal2%s.csv'%(protein+str(i))
		# print files
		# print my_file
		if os.path.exists(my_file) == True:
			print 'jeej'
				# print 'result_anneal2%s'%(protein+str(i))

