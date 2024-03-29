from classes import amino_acid
import numpy
import string
import functions
import copy
import main_new
import random


def build(protein):
	len_proteinsh = len(protein) -2
	direction = [0] * len_proteinsh
	best_score = 0
	best_direction = []
	best_grid = []
	number = -1
	big = 1
	next_big = 4
	r = 1
	number_range = 4**len_proteinsh /2

	while number < number_range:
		number += 1
		stop = False
		leftover = number
  		index = 0
  		prev_number = 10
  		# print number
  		while(leftover > 0):
  			getal = leftover%4
  			direction[len_proteinsh - index - 1] = getal
  			index +=1
  			if abs(getal - prev_number) == 2:
  				number += 4**(index-2) -1
  				stop = True
  				break
  			if index == r and getal == 3:
  				number += big
  				stop = True
  				break
  			leftover /=4
  			prev_number = getal

  		if stop == True:
  			continue
  		if number >= next_big:
  			r += 1
  			next_big = 4**r
  			big = 4**(r-1)
		result = place(protein, direction, len_proteinsh)

		if result[0] < best_score:
			best_score = result[0]
			best_direction = copy.copy(result[1])
			best_grid = copy.copy(result[2])

	make_vis(protein, best_direction, len_proteinsh, best_score)
	return [best_score, best_direction, best_grid]

def place(protein, direction, length):
	for num in range(length):
		rotate = direction[num]
		# rotate 0 = rechts
		if rotate == 0:
			x = protein[num + 1].coordinates[0] + 1
			y = protein[num + 1].coordinates[1]
	
		#direction 1 = up
		elif rotate == 1:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] + 1
		# direction 2 = left
		elif rotate == 2:
			x = protein[num + 1].coordinates[0] - 1
			y = protein[num + 1].coordinates[1]
	
	# direction 3 = down
		else:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] - 1
		
		for j in range(num + 2):
			if protein[j].coordinates[0] == x and protein[j].coordinates[1] == y:
				return [1,1,1]

		protein[num + 2].coordinates[0] = x
		protein[num + 2].coordinates[1] = y
	
	grid =  functions.protein_visual(protein)
	score = functions.score(protein, grid)
	return [score, direction, grid, protein]


def make_vis(protein, direction, length, score):
	for num in range(length):
		rotate = direction[num]
		# rotate 0 = rechts
		if rotate == 0:
			x = protein[num + 1].coordinates[0] + 1
			y = protein[num + 1].coordinates[1]
	
		#direction 1 = up
		elif rotate == 1:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] + 1
		# direction 2 = left
		elif rotate == 2:
			x = protein[num + 1].coordinates[0] - 1
			y = protein[num + 1].coordinates[1]
	
	# direction 3 = down
		else:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] - 1
		
		for j in range(num + 2):
			if protein[j].coordinates[0] == x and protein[j].coordinates[1] == y:
				return [1,1,1]

		protein[num + 2].coordinates[0] = x
		protein[num + 2].coordinates[1] = y
	
	functions.Visualizer2D(protein, main_new.protein, score, 2000)

def theo_score(protein):
	odd_count = 0
	even_count = 0

	for i in range(len(protein)):
		if protein[i] == 'H':
			if i == 0:
				even_count += 3
				# print 'even 3'
			elif len(protein) % 2 == 0 and i == len(protein) - 1:
				odd_count += 3
				# print 'even 3'
			elif i == len(protein) - 1:
				even_count += 3
			elif i % 2 == 0:
				even_count += 2
			else:
				odd_count += 2

	odds_ratio = even_count/odd_count

	if odd_count < even_count:
		return len(protein), odd_count, odds_ratio
	else:
		return len(protein), even_count, odds_ratio

def random_protein(protein):
	print 'I am here'
	len_proteinsh = len(protein) -2
	direction = [0] * len_proteinsh
	valid = False
	while valid == False:
		stop = False	
		i = 0
		while i < len_proteinsh:
			if i == 0:
				direction[i] == random.randint(0,1)
			else:
				direction[i] = random.randint(0,3)
				if abs(direction[i] - direction[i-1]) == 2:
					continue
			i += 1
		print direction
		result = place(protein, direction, len_proteinsh)
		print result
		if result[0] != 1:
			valid = True
	return result