import numpy, string, functions, copy, csv, random, main_iter
from classes import amino_acid
from functions import protein_place
from timeit import default_timer as timer

# folds given amino acid 90 degrees respectively to the old angle of the precursor string
def fold_amino(coor_array, new_coor, amino_num):

	# gets direction vector for x and y between amino number and amino number - 1
	vec_x = coor_array[amino_num][0] - coor_array[amino_num - 1][0]
	vec_y = coor_array[amino_num][1] - coor_array[amino_num - 1][1]

	# all possible turns [x + 1 , y], [x, y + 1], [x - 1, y], [x, y - 1]] 
	if vec_x > 0:
		update_coor = [new_coor[0], new_coor[1] + 1]

	elif vec_x < 0:
		update_coor = [new_coor[0], new_coor[1] - 1]

	elif vec_y > 0:
		update_coor = [new_coor[0] - 1, new_coor[1]]

	elif vec_y < 0:
		update_coor = [new_coor[0] + 1, new_coor[1]]

	return update_coor

# folds given amino acid and rest string 90 degrees clockwise 	
def update_objects(protein_object, new_array):
	for i in range(len(protein_object)):
		protein_object[i].coordinates = new_array[i]
	return protein_object

# creates array of coordinates from protein_object array
def get_coor_array(protein_object):
	coor_array = []
	for amino in protein_object:
		coor_array.append(amino.coordinates)
	return coor_array


# initiates folding by taking protein_object as argiment
def folder_protein(coor_array, amino_num, turn):

	# length of protein_object/coor_array
	len_protein = len(coor_array)
	
	# copies values from coor_array
	new_array = copy.copy(coor_array)
	temp_array = copy.copy(coor_array)

	repeat = False

	# zeroes list for repeated turns per amino acids
	rep_list = [0] * len(coor_array)

	while repeat == False:
		repeat = True
		i = 0

		for i in range(turn):
		# folds complete string starting from amino num
			while i < len(coor_array) - amino_num:

				new_array[amino_num + i] = fold_amino(temp_array, new_array[amino_num + (i - 1)], amino_num + i)
				i += 1

		# checks if coordinates are shared by multiple amino acids
		for j in range(len(coor_array) - amino_num):
			if new_array[amino_num + j] in new_array[0:amino_num + j]:
				temp_array = copy.deepcopy(new_array)

				if j == 0:
					rep_list[amino_num] += 1

				# if amino number is folded more than 3 times, previous amino acid is folded
				if rep_list[amino_num + j] >= 3 and amino_num > 2:
					amino_num = amino_num + j - 1
					repeat = False
					break
				
				# amino num 0 and 1 won't be folded to minimalize the number of rotations
				elif rep_list[amino_num + j] >= 3 and amino_num <= 2:
					return coor_array
				
				# if coordinates are shared amino acid is folded 
				else:	
					amino_num = copy.copy(amino_num + j)
					repeat = False
					turn = 1
					break
			
	return new_array

# finds lowest score of rep_num folds of single protein
def find_best(protein_object, rep_num, high_score):
	
	# array with times and iterations
	result_array = []
	start = timer()
	result_array.append(['start', start])
	
	high_protein_object = copy.deepcopy(protein_object)
	high_coor_array = []

	coor_array = get_coor_array(protein_object)

	count = 0
	rep_count = 0

	# folds random amino acid rep_num times 
	# rep_count checks if protein changes and returns 
	# best protein if protein stays the same after 30 folds
	while count < rep_num and rep_count < 50:
		start_ran = timer() - start
		fold_coor = folder_protein(coor_array, random.randint(2, len(coor_array) - 1)) 
		protein_object_new = update_objects(protein_object, fold_coor)
		grid = functions.protein_visual(protein_object_new)
		score = functions.score(protein_object_new, grid)

		#  checks if coordinates stay the same (no change)
		if fold_coor == coor_array:
			rep_count += 1
		else:
			coor_array = copy.deepcopy(fold_coor)
			count += 1
		
		# updates high score and object that belongs to high score 
		if score < high_score:
			high_score = copy.copy(score)
			high_protein_object = copy.deepcopy(protein_object_new)
			high_coor_array = copy.deepcopy(coor_array)

		# adds end time and score after every fold set completion
		end_ran = timer() - start
		result_array.append(['best ran', start_ran, end_ran, count + rep_count, high_score])

	end = timer()
	result_array.append(['end', end])

	return [high_score, high_protein_object]

# finds best protein fold when only P's are folded
def find_best_p(protein_object, rep_num, best_score):
	result_array = []
	start = timer()
	result_array.append(['start', start])
	high_protein_object = copy.deepcopy(protein_object) 
	
	# arrays with h, p and c amino acid chain numbers
	h_loc = []
	p_loc = []
	c_loc = []

	# gets coordinates array
	coor_array = get_coor_array(protein_object)

	# fills H and P arrays
	for i in range(len(protein_object)):
		if protein_object[i].ac_type == 'H':
			h_loc.append(i)
		elif protein_object[i].ac_type == 'P':
			p_loc.append(i)
		elif protein_object[i].ac_type == 'C':
			c_loc.append(i)

	count = 0
	rep_count = 0

	# folds random P amino acid rep_num times
	# rep_count checks if protein changes and returns 
	# best protein if protein stays the same after 30 folds
	while count < rep_num and rep_count < 30:
		start_p = timer() - start
		random_bend = 0

		# gets random amino num form p array (not amino num 0 and 1)
		while random_bend == 0 or random_bend == 1:
			random_bend = random.choice(p_loc)

		# bool to chose between two folds or one
		rand_bool = random.randint(0, 1)

		# if two P's are next to each other the both get folded to form a U turn
		if random_bend + 1 in p_loc and rand_bool == 1:

			# folds amino num, amino num + 1
			for i in range(2):
				fold_coor = folder_protein(coor_array, random_bend)
				protein_object_new = copy.deepcopy(update_objects(protein_object, fold_coor))
				grid = functions.protein_visual(protein_object_new)
				score = functions.score(protein_object_new, grid)
				
				if fold_coor == coor_array:
					rep_count += 1
				else:
					coor_array = copy.deepcopy(fold_coor)
				count += 1
				random_bend += 1

				# checks if current score is new high score and updates score + object
				if score < best_score:
					best_score = copy.copy(score)
					best_protein_object = copy.deepcopy(protein_object_new)
		
		# folds random amino num 
		else:
			fold_coor = folder_protein(coor_array, random_bend)
			protein_object_new = copy.deepcopy(update_objects(protein_object, fold_coor))
			grid = functions.protein_visual(protein_object_new)
			score = functions.score(protein_object_new, grid)
			protein_object = copy.deepcopy(protein_object_new)
			
			# only updates coor array if it differs from previous coor array
			if fold_coor == coor_array:
					rep_count += 1
			else:
				coor_array = copy.deepcopy(fold_coor)
			count += 1
			
			if score < best_score:
					best_score = copy.copy(score)
					best_protein_object = copy.deepcopy(protein_object_new)
		
		# adds end time and score after every fold set completion
		end_p = timer() - start
		result_array.append(['get best P', start_p, end_p, count + rep_count, best_score])			
	
	end = timer()
	result_array.append(['end', end])

	return [best_score, best_protein_object]

# hillclimber for every start protein given
def hill_climber(start_array, fold_num):
	result_array = []
	i = 0
	start = timer()
	result_array.append(['start', start])

	# every start coordinates se
	while i < len(start_array):
		same = 0
		j = 0

		# keeps swapping with fold_num folds untill the high score is not changed for 30 times
		while same < 70:
			start_hill = timer() - start
			new_object = copy.deepcopy(start_array[i])
			new_object = find_best(new_object[1], fold_num, new_object[0])
			
			# checks if high score is the same
			if new_object[0] == start_array[i][0]:
				same += 1

			# resets repeat  
			else:
				start_array[i] = copy.deepcopy(new_object)
				same = 0
			
			# iterations and time in results array
			end_hill = timer() - start
			result_array.append(['hillclimber P', start_hill, end_hill, i*j, new_object[0]])
			j += 1
		i += 1
		print "Hillclimber succes"

	end = timer()
	result_array.append(['end', end])

	return start_array, result_array

# writes given results array to csv
def write_csv(in_array, csv_name):
	f = open('results/%s.csv' % csv_name, 'w')
	csv_file = csv.writer(f, delimiter = ',')
	for row in in_array:
		csv_file.writerow(row)

# gets best result from all hillclimbers and saves image
def visual_array_result(protein_array, protein, name):
	best = 0
	best_object = []
	for item in protein_array:
		if item[0] < best:
			best = copy.deepcopy(item[0])
			best_object = copy.deepcopy(item[1])
	functions.Visualizer2D(best_object, protein, best, name)
	return [best, best_object]

# gets array of start positions with best scores starting from straight string
def get_start(protein_object, rep_num, start_num, function):
	high_score = 0
	start_array = []
	for i in range(start_num):
		print i
		temp_array = function(protein_object, rep_num, high_score)
		start_array.append(temp_array)
	return start_array

def random_sampling(protein, configurations, fold_factor):
	protein_coor = get_coor_array(protein)
	len_protein = len(protein_coor)
	print len_protein
	protein_array = []
	j = 0 
	while j < configurations:
		folds = random.randint(0, fold_factor*len_protein)
		print folds
		start_coor = copy.deepcopy(protein_coor)
		# print start_coor
		for i in range(folds):
			new_coor = folder_protein(start_coor, random.randint(2,len_protein), random.randint(1,3))
			# print 'made fold'
			start_coor = copy.deepcopy(new_coor)
		new_protein = update_objects(protein, new_coor)
		# print 'made protein'
		grid = functions.protein_visual(new_protein)
		score = functions.score(new_protein, grid)
		protein_info = [score, copy.deepcopy(new_protein)]
		# print new_protein
		if protein_info not in protein_array:
			# print 'unique'
			protein_array.append(protein_info)
			j += 1
		else:
			# print 'not unique'
			print protein_info
			print protein_array

	return protein_array

