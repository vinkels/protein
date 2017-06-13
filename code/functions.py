import numpy, string, csv
from classes import amino_acid
import matplotlib.pyplot as plt

# gives protein coordinates for straight horizontal string
def protein_place(protein):
	protein_object = []
	len_protein = len(protein)
	for i in range(len_protein):
		
		if protein[i] == 'H' or protein[i] == 'C':
			if i == 0 or i == len(protein)-1:
				protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein)], 3))
			else:
				protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein)], 2))
		elif protein[i] == 'P':
			protein_object.append(amino_acid(i, protein[i], [len(protein) + i, len(protein)], 0))
	return protein_object	

# 2D visualizer of protein object, saves as png image
def Visualizer2D(protein_object, protein, protein_score, name):
	plt.close()
	x = []
	y = []

	for item in protein_object:
		x.append(item.coordinates[0])
		y.append(item.coordinates[1])

	col = []
	size = 5000/len(protein)

	# Zet het kleuren array
	for amino in protein:
		if amino == 'H':
			col.append('b')
		elif amino == 'P':
			col.append('y')
		elif amino == 'C':
			col.append('r')


	ax = plt.plot(x, y, 'k', zorder=1, lw=3)
	bx = plt.scatter(x, y, s=size, zorder=2, c=col)
	plt.title('protein: %s \n Score = %s' %(protein, protein_score))
	plt.axis('off')
	plt.savefig('results/fold_%s.png' %name)
	plt.figure()
	plt.close()

# creates numpy plot of protein object
def protein_visual(protein_object):
	len_protein = len(protein_object)
	grid = numpy.chararray((2*len_protein+1, 2*len_protein+1), itemsize=2)
	grid[:] = '..'
	for i in range(len_protein):
		name_loc = protein_object[i].ac_type + str(protein_object[i].chain_loc)
		loc = protein_object[i].chain_loc
		x_coor = protein_object[i].coordinates[0]
		y_coor = protein_object[i].coordinates[1]
		grid[y_coor, x_coor] = name_loc
	return grid

# calculates score of protein object by using grid coordinates
def score(protein_object, grid):
	score = 0
	len_protein = len(protein_object)
	for i in range(len_protein):
		x = protein_object[i].coordinates[1]
		y = protein_object[i].coordinates[0]
		if protein_object[i].ac_type == 'H':
			if grid[x+1][y][0] == 'H' or grid[x+1][y][0] =='C':
				score -= 1
			if grid[x-1][y][0] == 'H' or grid[x-1][y][0] == 'C': 
				score -= 1
			if grid[x][y+1][0] == 'H' or grid[x][y+1][0] == 'C': 
				score -= 1
			if grid[x][y-1][0] == 'H' or grid[x][y-1][0] == 'C':
				score -= 1
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'H' or protein_object[i + 1].ac_type == 'C'):
				score += 1
			if i != 0 and (protein_object[i - 1].ac_type == 'H' or protein_object[i - 1].ac_type == 'C'):
				score += 1

		if protein_object[i].ac_type == 'C':
			if grid[x+1][y][0] == 'H':
				score -= 1
			if grid[x-1][y][0] == 'H': 
				score -= 1
			if grid[x][y+1][0] == 'H': 
				score -= 1
			if grid[x][y-1][0] == 'H':
				score -= 1
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'H'):
				score += 1
			if i != 0 and (protein_object[i - 1].ac_type == 'H'):
				score += 1
			if grid[x+1][y][0] == 'C':
				score -= 5
			if grid[x-1][y][0] == 'C': 
				score -= 5
			if grid[x][y+1][0] == 'C': 
				score -= 5
			if grid[x][y-1][0] == 'C':
				score -= 5
			if i != len_protein-1 and (protein_object[i + 1].ac_type == 'C'):
				score += 5
			if i != 0 and (protein_object[i - 1].ac_type == 'C'):
				score += 5
	score = score/2
	return score		

def extract_protein():

	# f = open(csv_name, 'r')
	f = open('results/constructive_random1.csv','r')
	data = csv.reader(f, delimiter=',')
	protein_array = []
	for row in data:
		protein_array.append(row[3])

	return protein_array
