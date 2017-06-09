import numpy, string, functions, copy, csv, random, main_iter, folder_iter
from classes import amino_acid
from functions import protein_place
from timeit import default_timer as timer

def folder_direct(coor_array, amino_num, fold_direct):

	# length of protein_object/coor_array
	len_protein = len(coor_array)
	
	# copies values from coor_array
	new_array = copy.copy(coor_array)
	temp_array = copy.copy(coor_array)

	repeat = False

	# zeroes list for repeated turns per amino acids
	rep_list = [0] * len(coor_array)
	print rep_list
	rep_dir = fold_direct
	# print amino_num, fold_direct
	while repeat == False and rep_dir > 0:
		# print 'after break', rep_dir, amino_num
		repeat = True
		i = 0

		# folds complete string starting from amino num
		while i < len(coor_array) - amino_num:

			new_array[amino_num + i] = folder_iter.fold_amino(temp_array, new_array[amino_num + (i - 1)], amino_num + i)
			i += 1
			temp_array = copy.deepcopy(new_array)
		
		rep_dir -= 1	
		print rep_dir
		if rep_dir > 0:
			repeat = False
		elif rep_dir == 0:
			# print 'kom ik hier'
		# checks if coordinates are shared by multiple amino acids
			for j in range(len(coor_array) - amino_num - 1):
				if new_array[amino_num + j] in new_array[0:amino_num + j]:
					temp_array = copy.deepcopy(new_array)

					if j == 0:
						rep_list[amino_num] += 1

					# if amino number is folded more than 3 times, previous amino acid is folded
					if rep_list[amino_num + j] >= 3 and amino_num > 2:
						amino_num = amino_num + j - 1
						repeat = False
						rep_dir = 1
						print 'is het te kort'
						# print 'before break'
						break
					
					# amino num 0 and 1 won't be folded to minimalize the number of rotations
					elif rep_list[amino_num + j] >= 3 and amino_num <= 2:
						print 'is het old array'
						return coor_array
					
					# if coordinates are shared amino acid is folded 
					else:	
						amino_num = amino_num + j
						repeat = False
						rep_dir = 1
						print 'is het dat het gewoon faalt'
						print amino_num + j
						# print rep_list[amino_num + j]
						# print 'before break'
						break
	
	return new_array