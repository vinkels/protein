import classes, functions, folder_iter, cProfile, copy, folder_iter, test, protein_generator

# protein = 'HPPHPPHPHPHPHPHPPHPHHPHPHPHHPPP'

def main():
	length = 20
	h_concentration = 5
	protein_array = copy.copy(protein_generator.protein_generator(length, h_concentration, 3))
	result_array = []
	for protein in protein_array:
		protein_object = functions.protein_place(protein)
		print protein_object
		configurations = 3
		start_pos = folder_iter.random_sampling(protein_object, 3, configurations)
		folder_iter.write_csv(start_pos, 'random_sampling%s' %protein)
		theo = test.theo_score(protein)
		score_saver = [protein, configurations] + [0]*(theo[0]+1)
		print score_saver
		# score_saver.append(configurations)
		# score_saver.append([0]*(theo[0]+1))
		for result in start_pos:
			score_saver[abs(result[0])+2] += 1
		high_score = protein_generator.highscorefreq(score_saver)
		result_array.append(score_saver)
	folder_iter.write_csv(result_array, 'randomsampling_overview%s_%s' %(length, h_concentration))
	# print start_pos
	
if __name__ == '__main__':
	# cProfile.run('main(protein)')
	main() 
	