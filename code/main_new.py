import classes, functions, test, folder_3d, functions_3d, cProfile, score_saver
from timeit import default_timer as timer

protein ="HHPHHHPHPHHHPHHP"

#"HPHPPHHPHPPHPHHPPHPH"

#109.9s HHPHHHPHPHHHPH
# PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
def main(protein):
	result_array = []
	start = timer()
	result_array.append(['start', start])
	placed_protein = functions.protein_place(protein)
	theo = test.theo_score(protein)
	score_saver.build(placed_protein, theo)
	end = timer() - start
	result_array.append(['end', end])


	# print result_array
	

if __name__ == '__main__':
	# cProfile.run('main(protein)')
	main(protein)