import classes, functions, folder_iter, cProfile, copy, folder_iter, simulated_annealing


protein = "HHPHPHPHPHHHHPPPHPPPHPPPPHPPPHPPPHPHPHHHHHPHPHPHH"
# score found -21, Shmygelska, 2005, 

def main(protein):
	print len(protein)
	protein_object = functions.protein_place(protein)
	new_protein = simulated_annealing.anneal(protein_object, 'test1', 1)
	functions.Visualizer2D(new_protein[1], protein, new_protein[0], 'test1')

if __name__ == '__main__':
	main(protein)