from utils import *
from itertools import count

class MapAlgorithm:
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

	def create_nodes(self):
		for i in range(self.map_copy.size[0]):
			for j in range(self.map_copy.size[1]):
				new_node = Node((i, j), self.map_copy.map_array[i][j])
				self.map_nodes[(i, j)] = new_node

	def search(self):
		pass # will be overriden by inherited classes

	def visit(self, node):
		pass # will be overriden by inherited classes

	def print_debug(self):
		if self.path_modified == False:
			print("null")
		else:
			print("path:")
			self.print_path()
		print("#visits:")
		self.print_map(self.visits)
		print("first visit:")
		self.print_map(self.first_visit)
		print("last visit:")
		self.print_map(self.last_visit)

	def print_release(self):
		if self.path_modified == False:
			print("null")
		else:
			self.print_path()

	def print_path(self):
		for m in range(self.map_copy.size[0]):
			row_string = ""
			for n in range(self.map_copy.size[1]):
				num_string = ""
				num_string += str(self.path[m][n])
				row_string += num_string
				if (n < self.map_copy.size[1] - 1):
					row_string += " "
			print(row_string)

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

	# makes a copy from dictionary - able to modify costs, etc.
	def get_node(self, position):
		try:
			if self.map_nodes[position].elevation == "X" :
				return None
		except KeyError: #not in map
			return None
		return(PathNode(self.map_nodes[position]))

	# gets singular child node from a given parent and position
	def get_child_node(self, node_parent, position):
		child_node = self.get_node(position)

		if child_node != None:
			child_node.parent = node_parent

		return (child_node)

	# adds deep copies of node children to node parent's child array
	def get_node_children(self, node_parent):
		child_arr = []
		up_position = (node_parent.node.position[0] - 1, node_parent.node.position[1])
		down_position = (node_parent.node.position[0] + 1, node_parent.node.position[1])
		left_position = (node_parent.node.position[0], node_parent.node.position[1] - 1)
		right_position = (node_parent.node.position[0], node_parent.node.position[1] + 1)
		directions = [up_position, down_position, left_position, right_position]

		for direction in directions:
			if self.in_parent_path(node_parent, direction) == False:
				child_node = self.get_child_node(node_parent, direction)
				if child_node is not None:
					child_arr.append(child_node)
		return(child_arr)

	def parse_path(self, node):
		current_node = node
		while current_node is not None:
			self.path_modified = True
			self.path[current_node.node.position[0]][current_node.node.position[1]] = "*"
			current_node = current_node.parent

	def get_cost(self, node_from, node_to):
		base_cost = 1
		if node_to.node.elevation > node_from.node.elevation:
			base_cost += (node_to.node.elevation - node_from.node.elevation)
		return (base_cost)
	
	def in_parent_path(self, parent_node, position):
		current_node = parent_node
		while current_node is not None:
			if position == current_node.node.position:
				return (True)
			current_node = current_node.parent
		return (False)

