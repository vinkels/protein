import classes, functions, folder_iter, cProfile, copy, folder_iter

protein = 'HPPHHPHPPHPHHPPH'

def main(protein):
	protein_object = functions.protein_place(protein[i])
	# start_array = folder_iter.get_start(protein_object, 150* len(protein[i]), 100 + (5 * len(protein[i]))/2, folder_iter.find_best)
	# hill_result = folder_iter.hill_climber(start_array, 20)
	best_result = folder_iter.visual_array_result(hill_result[0], protein[i], i + 51)