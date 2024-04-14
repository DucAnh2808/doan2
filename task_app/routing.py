import copy
import math
from collections import defaultdict
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



path_followed = []

agent_locations = [(16, 25), (7, 3), (28, 13), (20, 29), (1, 30), (7, 13), (29, 19), (17, 17), (25, 21), (17, 6), (10, 3), (5, 22), (17, 18), (30, 26), (2, 5), (6, 3), (5, 28), (23, 2), (18, 17), (31, 19)]
# target_locations = [(1, 1), (1, 3), (2, 4), (3, 2), (4, 4), (10,10), (20,20), (30, 30), (40, 40)]

task_lists = [((2, 2), (34, 24)), ((2, 4), (34, 30)), ((2, 6), (34, 28)), ((2, 8), (34, 20)), ((2, 10), (34, 4)), ((2, 12), (34, 26)), ((2, 14), (34, 8)), ((2, 16), (34, 14)), ((2, 18), (34, 24)), ((2, 20), (34, 18)), ((2, 22), (34, 26)), ((2, 24), (34, 12)), ((2, 26), (34, 18)), ((2, 28), (34, 2)), ((2, 30), (34, 16)), ((4, 2), (34, 20)), ((4, 4), (34, 6)), ((4, 6), (34, 16)), ((4, 8), (34, 30)), ((4, 10), (34, 22)), ((4, 12), (34, 2)), ((4, 14), (34, 26)), ((4, 16), (34, 14)), ((4, 18), (34, 24)), ((4, 20), (34, 4)), ((4, 22), (34, 8)), ((4, 24), (34, 26)), ((4, 26), (34, 10)), ((4, 28), (34, 24)), ((4, 30), (34, 6)), ((6, 2), (34, 24)), ((6, 4), (34, 28)), ((6, 6), (34, 26)), ((6, 8), (34, 20)), ((6, 10), (34, 30)), ((6, 12), (34, 26)), ((6, 14), (34, 22)), ((6, 16), (34, 30)), ((6, 18), (34, 18)), ((6, 20), (34, 26)), ((6, 22), (34, 16)), ((6, 24), (34, 26)), ((6, 26), (34, 16)), ((6, 28), (34, 14)), ((6, 30), (34, 16)), ((8, 2), (34, 10)), ((8, 4), (34, 26)), ((8, 6), (34, 24)), ((8, 8), (34, 10)), ((8, 10), (34, 30)), ((8, 12), (34, 24)), ((8, 14), (34, 4)), ((8, 16), (34, 16)), ((8, 18), (34, 10)), ((8, 20), (34, 26)), ((8, 22), (34, 20)), ((8, 24), (34, 26)), ((8, 26), (34, 2)), ((8, 28), (34, 20)), ((8, 30), (34, 28)), ((10, 2), (34, 10)), ((10, 4), (34, 20)), ((10, 6), (34, 24)), ((10, 8), (34, 28)), ((10, 10), (34, 14)), ((10, 12), (34, 12)), ((10, 14), (34, 2)), ((10, 16), (34, 22)), ((10, 18), (34, 26)), ((10, 20), (34, 30)), ((10, 22), (34, 10)), ((10, 24), (34, 8)), ((10, 26), (34, 26)), ((10, 28), (34, 12)), ((10, 30), (34, 16)), ((12, 2), (34, 12)), ((12, 4), (34, 16)), ((12, 6), (34, 12)), ((12, 8), (34, 8)), ((12, 10), (34, 28)), ((12, 12), (34, 18)), ((12, 14), (34, 20)), ((12, 16), (34, 26)), ((12, 18), (34, 24)), ((12, 20), (34, 14)), ((12, 22), (34, 16)), ((12, 24), (34, 30)), ((12, 26), (34, 24)), ((12, 28), (34, 28)), ((12, 30), (34, 24)), ((14, 2), (34, 24)), ((14, 4), (34, 12)), ((14, 6), (34, 16)), ((14, 8), (34, 4)), ((14, 10), (34, 10)), ((14, 12), (34, 28)), ((14, 14), (34, 16)), ((14, 16), (34, 30)), ((14, 18), (34, 22)), ((14, 20), (34, 24)), ((14, 22), (34, 10)), ((14, 24), (34, 18)), ((14, 26), (34, 22)), ((14, 28), (34, 4)), ((14, 30), (34, 22)), ((16, 2), (34, 14)), ((16, 4), (34, 26)), ((16, 6), (34, 24)), ((16, 8), (34, 18)), ((16, 10), (34, 26)), ((16, 12), (34, 6)), ((16, 14), (34, 24)), ((16, 16), (34, 26)), ((16, 18), (34, 28)), ((16, 20), (34, 30)), ((16, 22), (34, 14)), ((16, 24), (34, 14)), ((16, 26), (34, 30)), ((16, 28), (34, 22)), ((16, 30), (34, 20)), ((18, 2), (34, 8)), ((18, 4), (34, 12)), ((18, 6), (34, 16)), ((18, 8), (34, 2)), ((18, 10), (34, 2)), ((18, 12), (34, 8)), ((18, 14), (34, 24)), ((18, 16), (34, 10)), ((18, 18), (34, 22)), ((18, 20), (34, 4)), ((18, 22), (34, 30)), ((18, 24), (34, 28)), ((18, 26), (34, 28)), ((18, 28), (34, 24)), ((18, 30), (34, 8)), ((20, 2), (34, 12)), ((20, 4), (34, 10)), ((20, 6), (34, 22)), ((20, 8), (34, 28)), ((20, 10), (34, 28)), ((20, 12), (34, 6)), ((20, 14), (34, 20)), ((20, 16), (34, 6)), ((20, 18), (34, 4)), ((20, 20), (34, 4)), ((20, 22), (34, 18)), ((20, 24), (34, 20)), ((20, 26), (34, 10)), ((20, 28), (34, 6)), ((20, 30), (34, 20)), ((22, 2), (34, 16)), ((22, 4), (34, 8)), ((22, 6), (34, 20)), ((22, 8), (34, 16)), ((22, 10), (34, 18)), ((22, 12), (34, 20)), ((22, 14), (34, 12)), ((22, 16), (34, 12)), ((22, 18), (34, 2)), ((22, 20), (34, 4)), ((22, 22), (34, 30)), ((22, 24), (34, 24)), ((22, 26), (34, 8)), ((22, 28), (34, 24)), ((22, 30), (34, 24)), ((24, 2), (34, 20)), ((24, 4), (34, 20)), ((24, 6), (34, 22)), ((24, 8), (34, 20)), ((24, 10), (34, 6)), ((24, 12), (34, 26)), ((24, 14), (34, 26)), ((24, 16), (34, 30)), ((24, 18), (34, 28)), ((24, 20), (34, 10)), ((24, 22), (34, 10)), ((24, 24), (34, 10)), ((24, 26), (34, 20)), ((24, 28), (34, 26)), ((24, 30), (34, 8)), ((26, 2), (34, 18)), ((26, 4), (34, 20)), ((26, 6), (34, 22)), ((26, 8), (34, 24)), ((26, 10), (34, 18)), ((26, 12), (34, 6)), ((26, 14), (34, 26)), ((26, 16), (34, 20)), ((26, 18), (34, 10)), ((26, 20), (34, 10)), ((26, 22), (34, 24)), ((26, 24), (34, 18)), ((26, 26), (34, 18)), ((26, 28), (34, 22)), ((26, 30), (34, 6)), ((28, 2), (34, 14)), ((28, 4), (34, 30)), ((28, 6), (34, 8)), ((28, 8), (34, 2)), ((28, 10), (34, 6)), ((28, 12), (34, 6)), ((28, 14), (34, 12)), ((28, 16), (34, 4)), ((28, 18), (34, 8)), ((28, 20), (34, 8)), ((28, 22), (34, 26)), ((28, 24), (34, 12)), ((28, 26), (34, 20)), ((28, 28), (34, 8)), ((28, 30), (34, 24))]

target_locations = [task[0] for task in task_lists]
class route:
	def __init__(self, num_agents, num_targets, agent_loc, target_loc, unallocated_targets = [], cost_function=None):
		global path_followed
        
		self.num_agents = num_agents
		target_indices = {}
		for i in range(len(target_loc)):
			target_indices[target_loc[i]] = i + num_agents

		unallocated_targets = target_loc.copy()
		self.agents_targets = defaultdict(list)
		
		for i in range(num_agents):
			self.agents_targets[i] = []

		final_path = []

		while(len(unallocated_targets)>0):

			min_val = float('inf')
			index_dict = {}
			parent_agent = -1

			curr_target = unallocated_targets.pop(0)
			
			for agent in self.agents_targets.keys():
				self.vertices = 2 + len(self.agents_targets[agent])

				targets = self.agents_targets[agent].copy()
				targets.append(curr_target)
				
				g = [[0 for column in range(self.vertices)] for row in range(self.vertices)]
				target_index_here = {}
				target_index_here[agent_loc[agent]] = 0
				for i in range(len(targets)):
					target_index_here[targets[i]] = i + 1
				
				agent_ind = 0
				for k in self.agents_targets[agent]:			# k la storage location agent loc la vi tri aget
					g[agent_ind][target_index_here[k]] = self.distance(agent_loc[agent], k)
				
				g[agent_ind][agent_ind] = 0
				g[agent_ind][target_index_here[curr_target]] = self.distance(agent_loc[agent], curr_target)
				# print(g[agent_ind][target_index_here[curr_target]])
				for i in targets:
					for j in targets:
						# print("i la gì",i)
						# print("j la gì",j)
						g[target_index_here[i]][target_index_here[j]] = self.distance(i, j)
						g[target_index_here[j]][target_index_here[i]] = self.distance(j, i)
				
				weight, p, g1 = self.primMST(g)
				if(weight<min_val):
					min_val = weight
					parent_agent = agent
					index_dict = target_index_here
					parent = p
					graph = g1

			self.agents_targets[parent_agent].append(curr_target)
			
			for i1 in range(1, len(graph)):
				if(parent[i1]==None):
					continue
				vertex_1 = [loc for loc, index in index_dict.items() if index == parent[i1]]
				vertex_2 = [loc for loc, index in index_dict.items() if index == i1]
			
				# path = [vertex_1, vertex_2, graph[parent[i1]][i1]]
				path = [parent_agent, vertex_1, vertex_2]
				# print(graph[parent[i1]][i1])
				if(path not in final_path):
					final_path.append(path)

				# with open('log.txt', 'a') as f:
				# 	f.write("Agent: " + str(parent_agent) + "---" + " Path: " + str(path) + "\n")
				# print("Agent: ", parent_agent, "Path: ", path)
				# print(final_path)
		path_followed = final_path
		with open('log.txt', 'a') as f:
			f.write(str(final_path))

	def distance(self, x, y):
		return (x[0]-y[0])**2 + (x[1]-y[1])**2 

	def distance_2(self, x, y):
		return abs(x[0] - y[0]) + abs(x[1] - y[1])

	def manhattan_distance(self, point1, point2):
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
	def total_distance(self, agent_locations, task_lists):
		total_distances = []
		for agent_location, tasks in zip(agent_locations, task_lists):
			distance = self.manhattan_distance(agent_location, tasks[0])  # agent to point 1
			distance += self.manhattan_distance(tasks[0], tasks[1])  # point 1 to point 2
			distance += self.manhattan_distance(tasks[1], tasks[0])  # point 2 back to point 1
			total_distances.append(distance)
		return total_distances


	def printMST(self, parent, graph, V):
		for i in range(1, V):
			if(parent[i]==None):
				continue

	def minKey(self, key, mstSet, V): 

		min1 = float('inf')
		min_index = -1
		for v in range(V):
			if (key[v] < min1 and mstSet[v] == False): 
				min1 = key[v] 
				min_index = v
  
		return min_index

	def primMST(self, graph):
		V = len(graph)
		key = [float('inf')] * V
		parent = [None] * V
		key[0] = 0
		mstSet = [False] * V

		parent[0] = -1
		for cout in range(V):

			u = self.minKey(key, mstSet, V)
			 
			mstSet[u] = True
			for v in range(V): 
				if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]: 
					key[v] = graph[u][v] 
					parent[v] = u

		weight = 0 
		for i in range(1, V):
			if(parent[i]==None):
				continue
			weight += graph[parent[i]][i]
   
		return weight, parent, graph

g = route(len(agent_locations), len(target_locations), agent_locations, target_locations)
