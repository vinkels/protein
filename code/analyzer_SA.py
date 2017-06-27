import csv




def main():
	extract_proteins('analyze2_50_25_15_complete')

def extract_proteins(csv_name):
	protein_array = []
	high_array = []
	f = open('resultskort/ANALYSIS/%s.csv' % (csv_name),'r')
	data = csv.reader(f, delimiter=',')
	for row in data:
		if 'protein' not in row[0]:
			protein_array.append(row[0])
			high_array.append(row[2])
	result_array = []
	percentage_array = [['protein','percentage','iterations']]
	print high_array
	for i in range(len(protein_array)):
		result = extract_results(protein_array[i])
		percentage = extract_percentage(result,high_array[i])
		result_array += result
		percentage_array.append([protein_array[i]] + percentage)
	write_csv(result_array, 'ANALYSIS/SA_scorekort%s' %(csv_name))
	print percentage_array
	write_csv(percentage_array, 'ANALYSIS/SA_percentagekort%s' %(csv_name))

def extract_percentage(result, high_score):
	high = int(high_score)
	percentage = 0
	mean = 0
	# print result
	for row in result:
		if row[2] <= high:
			percentage +=1
			mean += row[3]
	if percentage != 0:
		mean = mean/percentage
	
	percentage = int((percentage/float(14))*100)
	return [percentage, mean]

	

def extract_results(csv_name):
	result_array = []
	for i in range(14):
		f = open('resultskort/result_anneal2%s%s.csv' % (csv_name, i),'r')
		data = csv.reader(f, delimiter=',')
		
		high_score = 0
		iteration = 0
		for row in data:
			if row[0] == 'Score Iteration':
				score = int(row[1])
				if score < high_score:
					high_score = copy.copy(score)
					iteration = int(row[2])


		result_array.append([csv_name,i, high_score, iteration])
	return result_array

def write_csv(in_array, csv_name):
	f = open('resultskort/%s.csv' % csv_name, 'w')
	csv_file = csv.writer(f, delimiter = ',')
	for row in in_array:
		csv_file.writerow(row)

print main()
