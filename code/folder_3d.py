
from classes import amino_acid
import numpy
import string
import functions_3d, main_new
import copy

def build(protein, i):
	len_proteinsh = len(protein) -2
	direction = [0] * len_proteinsh
	best_score = 0
	best_direction = []
	best_grid = []
	number = -1
	big = 1
	next_big = 6
	r = 1
	number_range = 6**len_proteinsh /3
	
	# every direction array is represented by a number 
	while number < number_range:
		# next number is generated
		number +=1
		stop = False
		leftover = number
  		index = 0
  		prev_number = 10
  		while(leftover > 0):
  			digit = leftover%6
  			direction[len_proteinsh - index - 1] = digit
  			index +=1
  			
  			# if the previous placed number is opposite direction, the direction array is tagged as 'stop'
  			if abs(digit - prev_number) == 3:
  				# print "ABS"
  				number += 3**(index-2) -1
  				stop = True
  				break

	  		if index == r and digit == 3:
  				# print "SIM"
  				number += 3*big
  				# print "IK ZIT HIER"
  				stop = True
  				break	

  			leftover /=6
  			prev_number = digit

  		
  		# when tagged as 'stop' the direction array won't be preformed
  		if stop == True:
  			continue

  		if number >= next_big:
  			r += 1
  			next_big = 6**r
  			big = 6**(r-1)
  		# the directionarray is tested and a score is given
		# print direction
		result = place(protein, direction, len_proteinsh)

		if result[0] < best_score:
			best_score = result[0]
			best_direction = copy.copy(result[1])
		
		
	#highscore and best direction are returned	
	make_vis(protein, best_direction, len_proteinsh, best_score, i)
	return [best_score, best_direction, best_grid]

def place(protein, direction, length):
	
	# every aminoacid location is updated starting with the third aminoacid
	for num in range(length):
		
		#every number in direction array is linked to a direction
		rotate = direction[num]
		
		# rotate 0 = rechts
		if rotate == 0:
			x = protein[num + 1].coordinates[0] + 1
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2]
	
		#direction 1 = up
		elif rotate == 1:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] + 1
			z = protein[num + 1].coordinates[2]

		#direction 2 = front
		elif rotate == 2:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2] + 1
		
		# direction 3 = left
		elif rotate == 3:
			x = protein[num + 1].coordinates[0] - 1
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2]
		
		# direction 4 = down
		elif rotate == 4:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] - 1
			z = protein[num + 1].coordinates[2]

		# direction 5 = back
		else:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] 
			z = protein[num + 1].coordinates[2] - 1
		
		#if there is of aminoacids the function is ended and marked as false (by 1's)
		for j in range(num + 2):
			if protein[j].coordinates[0] == x and protein[j].coordinates[1] == y and protein[j].coordinates[2] == z:
				return [1,1,1]

		#coordinates of aminoacid are updated
		protein[num + 2].coordinates[0] = x
		protein[num + 2].coordinates[1] = y
		protein[num + 2].coordinates[2] = z
	
	#score of protein is calculated
	grid =  functions_3d.protein_visual(protein)
	score = functions_3d.score(protein, grid)
	
	#score and direction array are returned
	return[score, direction]

def make_vis(protein, direction, length, score, i):
	for num in range(length):
		coordinates = []
		rotate = direction[num]
		# rotate 0 = rechts
		if rotate == 0:
			x = protein[num + 1].coordinates[0] + 1
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2]
	
		#direction 1 = up
		elif rotate == 1:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] + 1
			z = protein[num + 1].coordinates[2]

		#direction 2 = front
		elif rotate == 2:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2] + 1
		# direction 3 = left
		elif rotate == 3:
			x = protein[num + 1].coordinates[0] - 1
			y = protein[num + 1].coordinates[1]
			z = protein[num + 1].coordinates[2]
		# direction 4 = down
		elif rotate == 4:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] - 1
			z = protein[num + 1].coordinates[2]

		# direction 5 = back
		else:
			x = protein[num + 1].coordinates[0]
			y = protein[num + 1].coordinates[1] 
			z = protein[num + 1].coordinates[2] - 1
		
		#proteins are updated
		protein[num + 2].coordinates[0] = x
		protein[num + 2].coordinates[1] = y
		protein[num + 2].coordinates[2] = z

	# print protein
	functions_3d.Visualizer3D(protein, main_new.protein[i], score, i + 5050)
	
	