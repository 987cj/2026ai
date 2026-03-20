import utils
from collections import deque
from itertools import count

class BFS(utils.MapAlgorithm):
	def __init__(self, path_map):
		self.map_copy = path_map
		self.path = path_map.map_array
		self.path_modified = False
		self.visits = self._MapAlgorithm__create_empty_map()
		self.visits_index = 0
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.map_nodes = dict()
		self.search_array = []
		self.search_index = count(0) #keeps add order preserved in priorityqueue
		self.create_nodes()
		self.visited = set()

	
	def search(self):
		self.visits_index = 1
		self.search_array = deque()

		start_node = self.get_node(self.map_copy.start)
		if start_node == None: # start node is inaccessible
			return

		self.visit(start_node)

		while self.search_array:
			current_node = self.search_array.popleft()
			if self.visit(current_node) == True:
				self.parse_path(current_node)
				break
			self.visited.add(current_node.node.position)

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
		
		self.search_array.extend(self.get_node_children(node))

		return(False)

	def in_parent_path(self, parent_node, position):
		if position in self.visited:
			return True
		return False
