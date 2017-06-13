import csv

def main():
	f = open('results/constructive_random1.csv','r')
	data = csv.reader(f, delimiter=',')
	output = open('results/constructive_R2.csv', 'w')
	writer = csv.writer(output, delimiter =',')

	for row in data:
		score_count = 0
		raw_array = row[2].replace('[', '').replace(']', '').replace('\n','').split(',')
		for i in range(len(raw_array)):
			temp_array = []
			temp_array.extend((row[0],row[1], row[3], score_count,raw_array[i]))
			writer.writerow(temp_array)
			score_count += 1
if __name__ == '__main__':
	main()

#duration,time,distribution,protein