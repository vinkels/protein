import classes, functions, test, folder_3d, functions_3d, cProfile
from timeit import default_timer as timer

protein ="HHPHHHPHPHHHPHHP"

#"HPHPPHHPHPPHPHHPPHPH"

#109.9s HHPHHHPHPHHHPH
# PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
def main(protein):
	# result_array = []
	# start = timer()
	# result_array.append(['start', start])
	# placed_protein = functions.protein_place(protein)
	# test.build(placed_protein)
	# end = timer() - start
	# result_array.append(['end', end])


	# print result_array
	print test.theo_score(protein)

if __name__ == '__main__':
	# cProfile.run('main(protein)')
	main(protein)