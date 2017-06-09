import classes, functions, cProfile, copy, folder_iter, simulated_annealing


protein = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
# score found -21, Shmygelska, 2005, 

def main(protein):
	protein_object = functions.protein_place(protein)
	for i in range(20):
		new_protein = simulated_annealing.anneal(protein_object, 'test%s' %(130+i), 1)
		folder_iter.write_csv(new_protein[2], 'result_anneal%s' %(130+i))
		functions.Visualizer2D(new_protein[1], protein, new_protein[0], 'test%s' %(130+i))
		print 'hillclimber succes'

if __name__ == '__main__':
	main(protein)