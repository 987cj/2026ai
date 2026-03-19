import utils
from collections import deque

class BFS(utils.MapAlgorithm):
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
