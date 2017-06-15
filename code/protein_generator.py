import random
import math

def protein_generator(length, H_number, amount):
	protein_array = []
	numberofoptions = (math.factorial(length) / math.factorial(length - H_number))/2
	# print numberofoptions
	if numberofoptions < amount:
		return "INVALID"
	while amount > 0:
		protein = length*['P']
		location_array = []
		H = H_number
		while H > 0:
			place = random.randint(0,length-1)
			if place in location_array:
				continue
			else: 
				location_array.append(place)
				protein[place] = "H"
				H -=1
		protein = "".join(protein)
		reverse_protein = protein[::-1]
		if protein not in protein_array and reverse_protein not in protein_array:
			protein_array.append(protein)
			amount -= 1

	return protein_array


# def odd_even(protein):
# 	odd_count = 0
# 	even_count = 0

# 	for i in range(len(protein)):
# 		if protein[i] == 'H':
# 			if i == 0:
# 			elif i % 2 == 0:
# 				even_count += 1
# 			else:
# 				odd_count += 1

# 	return[even_count, odd_count]

def highscorefreq(array):
	high = 0
	score = 0
	if array[len(array) -1] != 0:
		return [array[len(array)-1], -len(array)]
	for i in range(len(array)):
		if (array[i] == 0 and array[i-1] != 0):
			high = array[i-1]
			score = -(i-1)
	return [high,score]

highscorefreq([0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
