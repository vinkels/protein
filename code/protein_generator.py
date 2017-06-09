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


# print protein_generator(8, 2, 100)

