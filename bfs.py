import copy
import utils

class BFS(utils.MapAlgorithm):
	def search(self):
		self.visits_index = 1

		start_node = self.get_node(self.map_copy.start)
		if start_node == None: # start node is inaccessible
			return
		start_node.path.append(start_node)
		start_node.path_set.add(self.map_copy.start)

		self.visit(start_node)

		while len(self.search_array) > 0:
			if self.visit(self.search_array[0]) == True:
				self.parse_path(self.search_array[0])
				break
			self.search_array.pop(0)
	
	def visit(self, node):
		if self.visits[node.position[0]][node.position[1]] == ".":
			self.visits[node.position[0]][node.position[1]] = 1
		else:
			self.visits[node.position[0]][node.position[1]] += 1
		if self.first_visit[node.position[0]][node.position[1]] is not int:
			self.first_visit[node.position[0]][node.position[1]] = self.visits_index
		self.last_visit[node.position[0]][node.position[1]] = self.visits_index

		self.visits_index += 1

		if node.position == self.map_copy.end:
			return(True)
		self.get_node_children(node)
		for child in node.children:
			child.cost += node.cost
		self.search_array.extend(node.children)

		return(False)

	def parse_path(self, node):
		for path_node in node.path:
			self.path[path_node.position[0]][path_node.position[1]] = "*"
