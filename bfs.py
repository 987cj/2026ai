import utils

class BFS(utils.MapAlgorithm):
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
		if self.visits[node.position[0]][node.position[1]] == ".":
			self.visits[node.position[0]][node.position[1]] = 1
		else:
			self.visits[node.position[0]][node.position[1]] += 1
		if self.first_visit[node.position[0]][node.position[1]] == ".":
			self.first_visit[node.position[0]][node.position[1]] = self.visits_index
		self.last_visit[node.position[0]][node.position[1]] = self.visits_index

		self.visits_index += 1

		if node.position == self.map_copy.end:
			return(True)
		
		for child in self.get_node_children(node):
			child.cost = node.cost + self.get_cost(node, child)
			self.search_array.put((1, next(self.search_index), child))

		return(False)
