import classes, functions, cProfile, copy, folder_iter, simulated_annealing


# protein = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
# score found -21, Shmygelska, 2005, 
protein = functions.extract_protein()

def main(protein):

	protein_array = copy.deepcopy(protein)
	for j in range(len(protein_array)):
		protein_object = functions.protein_place(protein_array[j])
		print 'protein_object made'
		for i in range(20):
			new_protein = simulated_annealing.anneal(protein_object, 'test%s' %(130+i), 1)
			# print 'new_protein made'
			folder_iter.write_csv(new_protein[2], 'result_anneal%s' %(protein_array[j]+str(i)))
			# print 'written to csv'
			functions.Visualizer2D(new_protein[1], protein_array[j], new_protein[0], 'anneal%s' %(protein_array[j]+str(i)))
			print 'hillclimber succes'

if __name__ == '__main__':
	main(protein)