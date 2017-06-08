import classes, functions, folder_iter, cProfile, copy, folder_iter


protein =["HPHPPHHPHPPHPHHPPHPH","PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP","PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP","CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC","HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH","HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"]
# protein =["HHPHHHPHPHHHPH","HPHPPHHPHPPHPHHPPHPH","PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP","PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP","CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC","HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH","HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"]


def main(protein):
	i = 1
	protein_object = functions.protein_place(protein[i])
	start_array = folder_iter.get_start(protein_object, 150* len(protein[i]), 100 + (5 * len(protein[i]))/2, folder_iter.find_best)
	hill_result = folder_iter.hill_climber(start_array, 20)
	best_result = folder_iter.visual_array_result(hill_result[0], protein[i], i + 51)
	folder_iter.write_csv(hill_result[1], 'result_hill%i' %(i + 51))

	protein_object = functions.protein_place(protein[i])
	start_array = folder_iter.get_start(protein_object, 150 * len(protein[i]), 100 + (5 * len(protein[i]))/2, folder_iter.find_best)
	hill_result = folder_iter.hill_climber(start_array, 10)
	best_result = folder_iter.visual_array_result(hill_result[0], protein[i], 'p'+str(i + 51))
	folder_iter.write_csv(hill_result[1], 'result_hill_p%i' %(i + 51))
	# hill climber start folds random
	# for i in range(3):
	# 	protein_object = functions.protein_place(protein[i])
	# 	start_array = folder_iter.get_start(protein_object, 125 * len(protein[i]), 20 + (5 * len(protein[i]))/2, folder_iter.find_best)
	# 	hill_result = folder_iter.hill_climber(start_array, 15)
	# 	best_result = folder_iter.visual_array_result(hill_result[0], protein[i], i)
	# 	folder_iter.write_csv(hill_result[1], 'result_hill%i' %(i))

	# hill climber start folds only P
	# for i in range(len(protein)):
	# 	protein_object = functions.protein_place(protein[i])
	# 	start_array = folder_iter.get_start(protein_object, 100 * len(protein[i]), 20 + (5 * len(protein[i]))/2, folder_iter.find_best)
	# 	hill_result = folder_iter.hill_climber(start_array, 10)
	# 	best_result = folder_iter.visual_array_result(hill_result[0], protein[i], 'p'+str(i + 11))
	# 	folder_iter.write_csv(hill_result[1], 'result_hill_p%i' %(i + 11))

if __name__ == '__main__':
	cProfile.run('main(protein)') 
	# main(protein)
