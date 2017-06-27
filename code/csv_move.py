import shutil
import os.path
import fnmatch
import csv
from pathlib import Path


def make_array():
	protein_array = []
	csv_name = 'analyze2_50_20_500'
	f = open('results/final/%s.csv' % (csv_name),'r')
	data = csv.reader(f, delimiter=',')



	for row in data:
		if row[0] != 'protein':
			protein_array.append(row[0])
			# print row[0]
	# print protein_array

	# print files

	protein_ar = []
	for i in range(13,14):
		for protein in protein_array:
			# print protein
			try: 
				f = open('results/SA_50_20_15/result_anneal%s%s.csv' % (protein, i),'r')
			except IOError:
				try:
					f = open('results/SA_50_20_15/result_anneal2%s%s.csv' % (protein, i),'r')
				except IOError:
					protein_ar.append(protein)
					print protein
					print 'missing ', protein, i

	print protein_ar
	return protein_ar



			# print 'result_anneal2%s'%(protein+str(i))

