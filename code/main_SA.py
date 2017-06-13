import classes, functions, simulated_annealing, cProfile, folder_iter, copy


def main(protein):

	protein_array = copy.deepcopy(protein)
	for i in range(4, len(protein)):
		best_score = 0
		best_protein = []
		for j in range(8):
			protein_object = functions.protein_place(protein[i])
			new_protein = simulated_annealing.anneal(protein_object, i+10*j, 1)
			print "result:"
			print i,new_protein[0], new_protein[1]
			# folder_iter.write_csv(new_protein[2], 'result_anneal%s' %(i+10*j))
			if new_protein[0]<best_score:
				best_score = new_protein[0]
				best_protein = copy.deepcopy(new_protein[1])
			functions.Visualizer2D(new_protein[1], protein[i], new_protein[0], i+10*j + 800)
		functions.Visualizer2D(best_protein, protein[i], best_score, i+10*j + 900)
if __name__ == '__main__':
	# cProfile.run('main(protein)') 
	main(protein)