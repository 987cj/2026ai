import utils
import copy
import math
from queue import PriorityQueue
from itertools import count

class AStar(utils.MapAlgorithm):
	def __init__(self, path_map, heuristic):
		self.map_copy = path_map
		self.heuristic = heuristic
		self.path = copy.deepcopy(path_map.map_array)
		self.visits = self._MapAlgorithm__create_empty_map()
		self.visits_index = 0
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.map_nodes = dict()
		self.map_heuristics = dict()
		self.search_array = PriorityQueue()
		self.search_index = count(0) #keeps add order preserved in priorityqueue
		self.create_nodes()
		self.__create_heuristics()

	def __create_heuristics(self):
		match self.heuristic:
			case "euclidean":
				for i in range(self.map_copy.size[0]):
					for j in range(self.map_copy.size[1]):
						euclidean_distance = math.dist((i, j), self.map_copy.end)
						self.map_heuristics[(i, j)] = euclidean_distance
			case "manhattan":
				for i in range(self.map_copy.size[0]):
					for j in range(self.map_copy.size[1]):
						manhattan_distance = abs(i - self.map_copy.end[0]) + abs(j - self.map_copy.end[1])
						self.map_heuristics[(i, j)] = manhattan_distance
			case _:
				utils.exit_program("Heuristic is not valid.")


	def search(self):
		self.visits_index = 1

		start_node = self.get_node(self.map_copy.start)
		if start_node == None: # start node is inaccessible
			return
		start_node.path_set.add(self.map_copy.start)

		self.visit(start_node)

		while not self.search_array.empty():
			current_node = self.search_array.get()[2]
			if self.visit(current_node) == True:
				self.parse_path(current_node)
				break
	
	def visit(self, node):
		if self.visits[node.node.position[0]][node.node.position[1]] == ".":
			self.visits[node.node.position[0]][node.node.position[1]] = 1
		else:
			self.visits[node.node.position[0]][node.node.position[1]] += 1
		if self.first_visit[node.node.position[0]][node.node.position[1]] == ".":
			self.first_visit[node.node.position[0]][node.node.position[1]] = self.visits_index
		self.last_visit[node.node.position[0]][node.node.position[1]] = self.visits_index

		self.visits_index += 1

		if node.node.position == self.map_copy.end:
			return(True)
		
		for child in self.get_node_children(node):
			child.path_cost = node.path_cost + self.get_cost(node, child) + self.map_heuristics[child.node.position]
			self.search_array.put((child.path_cost, next(self.search_index), child))

		return(False)