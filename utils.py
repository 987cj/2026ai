import sys
import copy


class PathMap:
	size = (0, 0)
	start = (0, 0)
	end = (0, 0)
	map_array =[[]]

class Node:
	def __init__(self, position, cost):
		self.position = position
		self.cost = cost
		self.children = []
		self.path = []
		self.path_set = set()

class MapAlgorithm:
	def __init__(self, path_map):
		self.map_copy = path_map
		self.path = path_map.map_array
		self.visits = self._MapAlgorithm__create_empty_map()
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.map_nodes = dict()
		self.search_array = []
		self.__create_nodes()
	
	def __create_empty_map(self):
		new_map = []
		for i in range(self.map_copy.size[0]):
			new_row = []
			for j in range(self.map_copy.size[1]):
				if self.map_copy.map_array[i][j] != "X":
					new_row.append(".")
				else:
					new_row.append("X")
			new_map.append(new_row)
		return(new_map)

	def __create_nodes(self):
		for i in range(self.map_copy.size[0]):
			for j in range(self.map_copy.size[1]):
				new_node = Node((i, j), self.map_copy.map_array[i][j])
				self.map_nodes[(i, j)] = new_node

	def search(self):
		pass # will be overriden by inherited classes

	def print_debug(self):
		print("path:")
		self.print_map(self.path)
		print("#visits:")
		self.print_map(self.visits)
		print("first visit:")
		self.print_map(self.first_visit)
		print("last visit:")
		self.print_map(self.last_visit)

	def print_release(self):
		self.print_map(self.path)

	def print_map(self, map_arr):
		max_digits = 0
		for i in range(self.map_copy.size[0]):
			for j in range(self.map_copy.size[1]):
				digits = len(str(map_arr[i][j]))
				if digits > max_digits:
					max_digits = digits
		
		for m in range(self.map_copy.size[0]):
			row_string = ""
			for n in range(self.map_copy.size[1]):
				num_string = ""
				digits = len(str(map_arr[m][n]))
				if digits < max_digits:
					for space in range(max_digits - digits):
						num_string += " "
				num_string += str(map_arr[m][n])
				row_string += num_string
				if (n < self.map_copy.size[1] - 1):
					row_string += " "
			print(row_string)

	# makes a deep copy from dictionary - able to modify costs, etc.
	def get_node(self, position):
		try:
			if type(self.map_nodes[position].cost) is not int:
				return None
		except KeyError: #not in map
			return None
		try:
			return(copy.deepcopy(self.map_nodes[position]))
		except Exception:
			exit_program("Node error occurred - cannot copy node")

	# gets singular child node from a given parent and position
	def get_child_node(self, node_parent, position):
		child_node = self.get_node(position)

		if child_node is not None:
			child_node.path = node_parent.path.copy()
			child_node.path.append(child_node)
			child_node.path_set = node_parent.path_set.copy()
			child_node.path_set.add(position)
			node_parent.children.append(child_node)

		return (child_node)

	# adds deep copies of node children to node parent's child array
	def get_node_children(self, node_parent):
		up_position = (node_parent.position[0] - 1, node_parent.position[1])
		right_position = (node_parent.position[0], node_parent.position[1] + 1)
		down_position = (node_parent.position[0] + 1, node_parent.position[1])
		left_position = (node_parent.position[0], node_parent.position[1] - 1)

		if up_position not in node_parent.path_set:
			self.get_child_node(node_parent, up_position)

		if right_position not in node_parent.path_set:
			self.get_child_node(node_parent, right_position)

		if down_position not in node_parent.path_set:
			self.get_child_node(node_parent, down_position)

		if left_position not in node_parent.path_set:
			self.get_child_node(node_parent, left_position)


class MapInputError(Exception):
	pass


def exit_program(message):
	print(message)
	sys.exit(1) 