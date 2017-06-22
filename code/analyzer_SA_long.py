import csv


def main():
	extract_proteins('analyze2_50_25_500')

def extract_proteins(csv_name):
	protein_array = []
	theo_array = []
	random_array = []
	f = open('results/final/%s.csv' % (csv_name),'r')
	data = csv.reader(f, delimiter=';')

	for row in data:
		if row[0] != 'protein':
			protein_array.append(row[0])
			theo_array.append(row[4])
			random_array.append(row[2])
	result_array = []
	percentage_array = [['protein','percentage_highestscore','iterations_highestscore', 'relative_percentage', 'percentage_random', 'percentage_theo']]
	print protein_array
	for i in range(len(protein_array)):
		result = extract_results(protein_array[i])
		percentage = extract_percentage(result)
		random_percentage = extract_percentage_divider(random_array[i], result)
		theo_percentage = extract_percentage_divider(theo_array[i], result)
		result_array += result
		percentage_array.append([protein_array[i]] + percentage+random_percentage+theo_percentage)
	write_csv(result_array, 'SA_protein_overview/SA_score%s' %(csv_name))
	print percentage_array
	write_csv(percentage_array, 'SA_protein_overview/SA_percentage%s' %(csv_name))


def extract_percentage_divider(divider, result):
	divider = - float(divider)
	total = 0
	for row in result:
		total += row[2]
	total = total/(20 * float(divider))
	return [total]


	

def extract_percentage(result):
	high = 0
	percentage = 0
	mean = 0
	total = 0
	print result
	for row in result:
		if row[2] < high:
			percentage = 0
			high = row[2]
			mean = 0
		if row[2] == high:
			percentage +=1
			mean += row[3]
		total += row[2]

	if percentage != 0:
		mean = mean/percentage
	
	total = total/(high*float(20))
	percentage = int((percentage/float(20))*100)
	return [percentage, mean, total]

	

def extract_results(csv_name):
	result_array = []
	for i in range(20):
		print csv_name
		f = open('results/SA_50_25/result_anneal%s%s.csv' % (csv_name, i),'r')
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
