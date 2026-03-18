import copy
import utils

class BFS(utils.MapAlgorithm):
	def search(self):
		visits_index = 1

		start_node = self.get_node(self.map_copy.start)
		if start_node == None: # start node is inaccessible
			return
		start_node.path.append(start_node)
		start_node.path_set.add(self.map_copy.start)

		self.visits[start_node.position[0]][start_node.position[1]] = visits_index
		self.first_visit[start_node.position[0]][start_node.position[1]] = visits_index

		self.get_node_children(start_node)
		for child in start_node.children:
			child.cost += start_node.cost
		self.search_array.extend(start_node.children)
		
