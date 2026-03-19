import utils

class BFS(utils.MapAlgorithm):
	def search(self):
		self.visits_index = 1

		start_node = self.get_node(self.map_copy.start)
		if start_node == None: # start node is inaccessible
			return

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
			self.search_array.put((1, next(self.search_index), child))

		return(False)
