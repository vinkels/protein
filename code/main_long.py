import classes, functions, cProfile, copy, folder_iter, simulated_annealing, protein_generator, test, csv


# protein = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
# score found -21, Shmygelska, 2005, 

def main():

	# length = 50
	# h_concentration = 30
	# protein_array = copy.copy(protein_generator.protein_generator(length, h_concentration, 100))
	# result_array = []
	# for protein in protein_array:
	# 	protein_object = functions.protein_place(protein)
	# 	print protein_object
	# 	configurations = 500
	# 	start_pos = folder_iter.random_sampling(protein_object, configurations, 5)
	# 	# folder_iter.write_csv(start_pos, 'random_sampling%s' %protein)
	# 	theo = test.theo_score(protein)
	# 	score_saver = [protein, configurations] + [0]*(theo[0]+1)
	# 	print score_saver
	# 	for result in start_pos:
	# 		score_saver[abs(result[0])+2] += 1
	# 	high_score = protein_generator.highscorefreq(score_saver)
	# 	result_array.append(score_saver)
	# folder_iter.write_csv(result_array, 'randomsampling_overview%s_%s' %(length, h_concentration))
	protein_array = ['PHPHPHHPHHPHHHHHHPPHHPPHPPPHPPHPHPPHPHPPPHPPPHHPHH']
	# # csv_name = 
	f = open('results/final/randomsampling_overview50_20.csv','r')
	data = csv.reader(f, delimiter=',')

	# for row in data:
	# 	if row[0] != 'protein':
	# 		protein_array.append(row[0])

	# print protein_array

	for j in range(len(protein_array)):
		protein_object = functions.protein_place(protein_array[j])
		print 'protein_object made'
		for i in range(14):
			new_protein = simulated_annealing.anneal(protein_object, 'test22%s' %(130+i), 1)
			# print 'new_protein made'
			folder_iter.write_csv(new_protein[2], 'result_anneal2%s' %(protein_array[j]+str(i)))
			# print 'written to csv'
			# functions.Visualizer2D(new_protein[1], protein_array[j], new_protein[0], 'anneal%s' %(protein_array[j]+str(i)))
			print 'SA succes'

if __name__ == '__main__':
	main()
