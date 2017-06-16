import csv, folder_iter



def write_results(csv_name, results):
	folder_iter.write_csv(result_array, 'SA_scores' %(length, h_concentration))

def extract_results(csv_name):
	result_array = []
	for i in range(20):
		f = open('results/result_anneal%s%s.csv' % (csv_name, i),'r')
		data = csv.reader(f, delimiter=',')
		
		high_score = 0
		iteration = 0
		for row in data:
			if row[0] == 'Score Iteration':
				score = int(row[1])
				if score < high_score:
					high_score = score
					iteration = int(row[2])


		result_array.append([i, high_score, iteration])

	return result_array

print extract_results('PPHPHHPHHPPPHH')