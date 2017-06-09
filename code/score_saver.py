from classes import amino_acid
import numpy
import string
import functions
import copy
import main_new


def build(protein, i, theoscore):
	len_proteinsh = len(protein) -2
	direction = [0] * len_proteinsh
	best_score = 0
	best_direction = []
	best_grid = []
	score_saver = (theoscore+1) * [0]
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
  		print number
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
		
		if result[0]<=0:
			score_saver[result[0]] += 1

		if result[0] < best_score:
			best_score = result[0]
			best_direction = copy.copy(result[1])
			best_grid = copy.copy(result[2])

	make_vis(protein, best_direction, len_proteinsh, best_score, i)
	return [best_score, best_direction, best_grid, score_saver]

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
	return [score, direction, grid]


def make_vis(protein, direction, length, score, i):
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
	
	functions.Visualizer2D(protein, main_new.protein[i], score, i + 5000)