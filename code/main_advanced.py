import classes, functions, folder_iter, cProfile, copy, folder_iter, simulated_annealing


protein = "HHPHPHPHPHHHHPPPHPPPHPPPPHPPPHPPPHPHPHHHHHPHPHPHH"
# score found -21, Shmygelska, 2005, 

def main(protein):
	for i in range(20):
		protein_object = functions.protein_place(protein)
		new_protein = simulated_annealing.anneal(protein_object, 'test%s' %i, 1)
		folder_iter.write_csv(new_protein[2], 'result_anneal%s' %i)
		functions.Visualizer2D(new_protein[1], protein, new_protein[0], 'test%s' %i)
		print 'hillclimber succes'

if __name__ == '__main__':
	main(protein)