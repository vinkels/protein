import classes, functions, cProfile, copy, folder_iter, simulated_annealing, protein_generator, test, csv

protein = 'HHHHHHHH'
protein_object = functions.protein_place(protein)
coor_array = folder_iter.get_coor_array(protein_object)
array_new = folder_iter.folder_protein(coor_array, 2, 1)
array_new_new = folder_iter.folder_protein(array_new, 3, 1)
array_more_new = folder_iter.folder_protein(array_new_new, 5, 1)
array_final = folder_iter.folder_protein(array_more_new, 7, 1)
new_object = folder_iter.update_objects(protein_object, array_final)
functions.Visualizer2D(new_object, protein, 0, 'testvoorpaper')

