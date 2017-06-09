import classes, functions, folder_iter, cProfile, copy, folder_iter, simulated_annealing, random, folder_dir

protein = "HHPHPHPHPHHHHPPPHPPPHPPPPHPPPHPPPHPHPHHHHHPHPHPHH"

def main(protein):
	new_object = functions.protein_place(protein)
	for i in range(50):
		functions.Visualizer2D(new_object, protein, 0, 'test%s' %(5000 + i))
		fold_dir = random.randint(1, 3)
		fold_num = random.randint(2, len(protein))
		print fold_dir, fold_num
		coor_array = folder_iter.get_coor_array(new_object)
		fold_protein = folder_dir.folder_direct(coor_array, fold_num, fold_dir)
		new_object = folder_iter.update_objects(new_object, fold_protein)
		functions.Visualizer2D(new_object, protein, 0, 'test%s' %(5050+i))
		print 'succesfull fold'

if __name__ == '__main__':
	main(protein)