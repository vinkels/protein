import classes, functions, test, folder_3d, functions_3d, cProfile, score_saver, protein_generator, folder_iter, copy
from timeit import default_timer as timer


#"HPHPPHHPHPPHPHHPPHPH"

#109.9s HHPHHHPHPHHHPH
# PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
protein_array = copy.copy(protein_generator.protein_generator(16, 8, 100))

def main():
	print protein_array
	result_array = []
	for i in range(len(protein_array)):
		start = timer()
		placed_protein = functions.protein_place(protein_array[i])
		# print placed_protein
		theo = test.theo_score(protein_array[i])
		result = score_saver.build(placed_protein, theo, protein_array[i])
		end = timer() - start

		result_array.append(['duration %s' %i, end, result[3], protein_array[i]])

		print 'construct succes'
	
	folder_iter.write_csv(result_array, 'constructive_random2')

	
	# print result[3]
	

if __name__ == '__main__':
	# cProfile.run('main(protein)')
	main()