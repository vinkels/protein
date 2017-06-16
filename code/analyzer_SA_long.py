import csv




def main():
	extract_proteins('analyze_50_25_500')

def extract_proteins(csv_name):
	protein_array = []
	ratio_array = []
	f = open('results/final/%s.csv' % (csv_name),'r')
	data = csv.reader(f, delimiter=',')

	for row in data:
		if row[0] != 'protein':
			protein_array.append(row[0])
	result_array = []
	percentage_array = [['protein','percentage','iterations']]
	for i in range(len(protein_array)):
		result = extract_results(protein_array[i])
		percentage = extract_percentage(result)
		result_array += result
		percentage_array.append([protein_array[i]] + percentage)
	write_csv(result_array, 'SA_protein_overview/SA_score%s' %(csv_name))
	print percentage_array
	write_csv(percentage_array, 'SA_protein_overview/SA_percentage%s' %(csv_name))




def extract_percentage(result):
	high = 0
	percentage = 0
	mean = 0
	print result
	for row in result:
		if row[2] < high:
			percentage = 0
			high = row[2]
			mean = 0
		if row[2] == high:
			percentage +=1
			mean += row[3]

	if percentage != 0:
		mean = mean/percentage
	
	percentage = int((percentage/float(20))*100)
	return [percentage, mean]

	

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


		result_array.append([csv_name,i, high_score, iteration])
	return result_array

def write_csv(in_array, csv_name):
	f = open('results/%s.csv' % csv_name, 'w')
	csv_file = csv.writer(f, delimiter = ',')
	for row in in_array:
		csv_file.writerow(row)

print main()
