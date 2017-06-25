import random, copy, math
import folder_iter, main_SA, functions
from timeit import default_timer as timer

def anneal(protein_object, name, temperature):
	result_array = []
	cur_score = 0
	start = timer()
	result_array.append(['start', start])
	# make starting point
	# cur_protein_array = folder_iter.find_best(protein_object, rep_num, 0)
	# cur_score = cur_protein_array[0]
	cur_protein = copy.deepcopy(protein_object)
	cur_coor = folder_iter.get_coor_array(cur_protein)
	start_temp = temperature
	#set high_score
	high_score = cur_score
	high_protein = copy.deepcopy(cur_protein)
	j = 0
	# i = 0
	counter = 0 
	while j < 20:
		start_an = timer() - start
		# functions.Visualizer2D(cur_protein, 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', cur_score, "test%s+%s" %(i,counter))
		# i+=1
		result_array.append(['Start Anneal', start_an, temperature])
		while temperature > 0.01:
			# functions.Visualizer2D(cur_protein, 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', cur_score, "test%s+%s" %(i,counter))
			# i+=1

			# make next protein object
			next_coor = folder_iter.folder_protein(cur_coor, random.randint(2,len(protein_object) - 1), random.randint(1,3))
			next_protein = folder_iter.update_objects(protein_object, next_coor)
			next_grid = functions.protein_visual(next_protein)
			next_score = functions.score(next_protein, next_grid)

			# calculate acceptation_chance
			acceptation_chance = calc_chance(next_score, cur_score, temperature)
		
		# print acceptation_chance
			if acceptation_chance < temperature:
				# print "CHANGE"
				cur_score = next_score
				cur_protein = copy.deepcopy(next_protein)
				cur_coor = copy.deepcopy(next_coor)

			# temperature is updated (not in function, because it is more effort, lines of code and time)
			temperature -= temperature * 0.005
			# print "temperature:" + str(temperature)
		
			# print temperature
			if cur_score < high_score:
				# print "NEW HIGHSCORE"
				high_score = copy.copy(cur_score)
				high_protein = copy.deepcopy(cur_protein)
				result_array.append(['Score Iteration', high_score, counter, temperature])
			

			counter += 1
			# print cur_score, next_score, high_score, acceptation_chance
		cur_protein = copy.deepcopy(high_protein)
		cur_score = high_score
		cur_coor = folder_iter.get_coor_array(high_protein)
		start_temp = start_temp * 1.1
		temperature = start_temp
		end = timer() - start
		result_array.append(['Result SA %s' %name, start_an, end, counter, high_score])
		j+=1
		# functions.Visualizer2D(cur_protein, main_SA.protein, cur_score, "test")

	return [high_score, high_protein, result_array]

def calc_chance(next_score, cur_score, temperature):
	if cur_score <0:
		score_ratio = next_score/float(cur_score)
		
	else: 
		if next_score == cur_score:
			score_ratio = 1
		else: 
			score_ratio = 20

	if score_ratio > 1:
		# print "BETER"
		acceptation_chance = 0
	elif score_ratio == 1:
		acceptation_chance = random.random() * temperature * 2
	else:
		acceptation_chance = random.random() * 20/(1+math.exp(-100*score_ratio))
	return acceptation_chance

def fold_direction():
	random.randint(0, 4)
