import functions, folder_iter
import csv, string, sys, copy

def main():

	protein_array = extract_protein('constructive_random1')
	h_count = 0
	protein_len = len(protein_array[0][0])
	for amino in protein_array[0][0]:
		if amino == 'H':
			h_count += 1

	analyze_array = []
	analyze_array.append(['protein', 'theo_score', 'high_score', 'min_bond', 'min_count', 'odd_even_bond', 'odd_even_count', 'even1', 'even2', 'even3', 'even4', 'odd1', 'odd2', 'odd3', 'odd4'])
	for protein in protein_array:

		analyze_array.append(protein + protein_analyze(protein[0]))
	write_csv(analyze_array, 'analyze_%s_%s'%(protein_len, h_count))



def protein_analyze(protein):
	odd_bond = 0
	even_bond = 0
	odd_count = 0
	even_count = 0

	# even first, even second, even third, even fourth, odd first, odd second, odd third, odd fourth
	divide_array = [0] * 8
	bucket_size = len(protein)/4

	for i in range(len(protein)):
		if protein[i] == 'H':
			if i == 0:
				even_bond += 3
				even_count += 1
				divide_array[0] += 1

			elif len(protein) % 2 == 0 and i == len(protein) - 1:
				odd_bond += 3
				odd_count += 1
				divide_array[7] += 1

			elif i == len(protein) - 1:
				even_bond += 3
				even_count += 1
				divide_array[3] += 1

			elif i % 2 == 0:
				even_bond += 2
				even_count += 1

				if i < bucket_size:
					divide_array[0] += 1
				elif i < 2 * bucket_size:
					divide_array[1] += 1
				elif i < 3 * bucket_size:
					divide_array[2] += 1
				else: 
					divide_array[3] += 1
			else:
				odd_bond += 2
				odd_count += 1

				if i < bucket_size:
					divide_array[4] += 1
				elif i < 2 * bucket_size:
					divide_array[5] += 1
				elif i < 3 * bucket_size:
					divide_array[6] += 1
				else: 
					divide_array[7] += 1

	odd_even_bond = float(odd_bond)/float(even_bond)
	odd_even_count = float(odd_count)/float(even_count)

	if odd_count < even_count:
		return [odd_bond, odd_count, odd_even_bond, odd_even_count] + divide_array
	else:
		return [even_bond, even_count, odd_even_bond, odd_even_count] + divide_array

def extract_protein(csv_name):

	# f = open(csv_name, 'r')
	f = open('results/%s.csv' % csv_name,'r')
	data = csv.reader(f, delimiter=',')
	protein_array = []
	for row in data:
		theo_score = 0
		high_score = 0
		scores = row[2].replace('"', '').replace('[', '').replace(']', '').split(",")

		theo_score = len(scores) - 1

		for i in range(theo_score + 1):
			if scores[i] != ' 0':

				high_score = copy.copy(i)

		protein_array.append([row[3], theo_score, high_score])

	return protein_array

def write_csv(in_array, csv_name):
	f = open('results/%s.csv' % csv_name, 'w')
	csv_file = csv.writer(f, delimiter = ',')
	for row in in_array:
		csv_file.writerow(row)





if __name__ == '__main__':
	main()