import classes, functions, test, folder_3d, functions_3d, cProfile
from timeit import default_timer as timer

protein =["HHPHHHPHPHHHPH","HPHPPHHPHPPHPHHPPHPH","PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP","PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP","CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC","HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH","HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"]


#109.9s HHPHHHPHPHHHPH
# PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
def main(protein):
	result_array = []
	for i in range(len(protein)):
		start = timer()
		result_array.append(['start', start])
		placed_protein = functions.protein_place(protein[i])
		test.build(placed_protein, i)
		end = timer() - start
		result_array.append(['end', end])

		start = timer()
		placed_protein = functions_3d.protein_place(protein[i])
		folder_3d.build(placed_protein, i)
		end = timer() - start
		result_array.append(['end', end])

	print result_array

if __name__ == '__main__':
	cProfile.run('main(protein)')