from classes import amino_acid
from mpl_toolkits.mplot3d import Axes3D
import numpy
import string
import matplotlib.pyplot as plt
import matplotlib as mpl

def protein_place(protein):
	protein_object = []
	len_protein = len(protein)
	for i in range(len_protein):
		
		if protein[i] == 'H' or protein[i] == 'C':
			if i == 0 or i == len(protein)-1:
				protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein), len(protein)], 3))
			else:
				protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein), len(protein)], 2))
		elif protein[i] == 'P':
			protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein), len(protein)], 0))
	return protein_object	



def Visualizer3D(protein_object, protein, protein_score, fold_num):
	plt.close()
	x = []
	y = []
	z = []
	a=protein
	for item in protein_object:
		x.append(item.coordinates[0])
		y.append(item.coordinates[1])
		z.append(item.coordinates[2])
	col = []
	score = protein_score/2
	size = 5000/len(a)

	# Zet het kleuren array
	for iets in a:
		if iets == "H":
			col.append('b')
		elif iets == "P":
			col.append('r')
		elif iets == "C":
			col.append('g')

	# x, y, z = [list(l) for l in zip(*protein_object)]

	fig = plt.figure()

	ax = fig.gca(projection='3d')
	ax.plot(x, y, z, 'k', zorder=1, lw=3)
	ax.scatter(x, y, z, s=size, zorder=2, c=col)
	plt.title('Best from constructive algorhythm\n Score = %s' %(protein_score))
	plt.axis('off')
	plt.savefig('results/fold_%s.png' %fold_num)
	plt.figure()
	plt.close()

def protein_visual(protein_object):
	len_protein = len(protein_object)
	grid = numpy.chararray((2*len_protein+1, 2*len_protein+1, 2*len_protein +1), itemsize=2)
	grid[:] = '..'
	for i in range(len_protein):
		name_loc = protein_object[i].ac_type + str(protein_object[i].chain_loc)
		loc = protein_object[i].chain_loc
		x_coor = protein_object[i].coordinates[0]
		y_coor = protein_object[i].coordinates[1]
		z_coor = protein_object[i].coordinates[2]
		grid[z_coor, y_coor, x_coor] = name_loc
	return grid


def score(protein_object, grid):
	score = 0
	len_protein = len(protein_object)
	for i in range(len_protein):
		x = protein_object[i].coordinates[1]
		y = protein_object[i].coordinates[2]
		z = protein_object[i].coordinates[0]
		if protein_object[i].ac_type == 'H':
			if grid[x+1][y][z][0] == 'H' or grid[x+1][y][z][0] =='C':
				score -= 1
				# print "x+1", x, y, grid[x+1][y][0], score
			if grid[x-1][y][z][0] == 'H' or grid[x-1][y][z][0] == 'C': 
				score -= 1
				# print "x-1", x, y, grid[x-1][y][0], score
			if grid[x][y+1][z][0] == 'H' or grid[x][y+1][z][0] == 'C': 
				score -= 1
				# print "y+1", x, y, grid[x][y+1][0], score
			if grid[x][y-1][z][0] == 'H' or grid[x][y-1][z][0] == 'C':
				score -= 1
			if grid[x][y][z + 1][0] == 'H' or grid[x][y][z + 1][0] == 'C': 
				score -= 1
				# print "y+1", x, y, grid[x][y+1][0], score
			if grid[x][y][z - 1][0] == 'H' or grid[x][y][z -1][0] == 'C':
				score -= 1
				# print "y-1", x, y, grid[x][y-1][0], score
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'H' or protein_object[i + 1].ac_type == 'C'):
				score += 1
			if i != 0 and (protein_object[i - 1].ac_type == 'H' or protein_object[i - 1].ac_type == 'C'):
				score += 1

		if protein_object[i].ac_type == 'C':
			if grid[x+1][y][z][0] == 'H':
				score -= 1
			if grid[x-1][y][z][0] == 'H': 
				score -= 1
			if grid[x][y+1][z][0] == 'H': 
				score -= 1
			if grid[x][y-1][z][0] == 'H':
				score -= 1
			if grid[x][y][z+1][0] == 'H': 
				score -= 1
			if grid[x][y][z-1][0] == 'H':
				score -= 1
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'H'):
				score += 1
			if i != 0 and (protein_object[i - 1].ac_type == 'H'):
				score += 1
			if grid[x+1][y][z][0] == 'C':
				score -= 5
			if grid[x-1][y][z][0] == 'C': 
				score -= 5
			if grid[x][y+1][z][0] == 'C': 
				score -= 5
			if grid[x][y-1][z][0] == 'C':
				score -= 5
			if grid[x][y][z -1][0] == 'C': 
				score -= 5
			if grid[x][y][z+1][0] == 'C':
				score -= 5
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'C'):
				score += 5
			if i != 0 and (protein_object[i - 1].ac_type == 'C'):
				score += 5
	score = score/2
	return score		

def start_score(protein_object):
	len_protein = len(protein_object)
	start_score = 0
	for i in range(len_protein):
		start_score += protein_object[i].bonds
	return start_score