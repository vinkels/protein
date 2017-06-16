import copy

row = [0, 3, 4, 0, 1, 6, 0, 20, 30]

high_score = 0
for i in range(len(row)):
	if row[i] != 0:

		high_score = copy.copy(i)

print high_score

string_num = ' 012983'

print int(string_num)