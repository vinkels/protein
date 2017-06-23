import networkx as nx
from networkx.algorithms import bipartite
import matplotlib
import copy

protein = 'HHPPHHHPHPHHPHH'
even_array = []
odd_array = []
theo_score = 0

for i in range(len(protein)):
		if protein[i] == 'H':
			if i % 2 == 0:
				even_array.append(i)
			else:
				odd_array.append(i)

connect_matrix = []
small_array = []
large_array = []

if len(even_array) < len(odd_array):
	small_array = copy.deepcopy(even_array)
	large_array = copy.deepcopy(odd_array)
else:
	small_array = copy.deepcopy(odd_array)
	large_array = copy.deepcopy(even_array)

for amino in small_array:
	if amino == 0 or amino == len(protein) - 1:
		theo_score += 3
	else:
		theo_score += 2


print theo_score, small_array, large_array

for i in range(len(small_array)):
	temp_array = [small_array[i]]
	for amino in large_array:
		if amino < small_array[i] - 2 and small_array[i] > 2:
			temp_array.append(amino)
		elif amino > small_array[i] + 2 and small_array[i] < len(protein) - 2:
			temp_array.append(amino)
	connect_matrix.append(temp_array)

print connect_matrix
unique_array = []
for connections in connect_matrix:
	if len(connections) < 3:
		theo_score -= 2 - len(connections)


# B = nx.Graph()
# B.add_nodes_from(even_array, bipartite=0) # Add the node attribute "bipartite"
# B.add_nodes_from(odd_array, bipartite=1)
# draw_networkx_nodes(G, pos[, nodelist, ...])
# B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])