import sys
import copy
from queue import PriorityQueue
from itertools import count


class PathMap:
	size = (0, 0)
	start = (0, 0)
	end = (0, 0)
	map_array =[[]]


class Node:
	def __init__(self, position, elevation):
		self.position = position
		self.elevation = elevation
		self.cost = 0

class PathNode:
	def __init__(self, node):
		self.node = node
		self.path_cost = 0
		self.path_set = set()


class MapAlgorithm:
	def __init__(self, path_map):
		self.map_copy = path_map
		self.path = copy.deepcopy(path_map.map_array)
		self.visits = self._MapAlgorithm__create_empty_map()
		self.visits_index = 0
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.map_nodes = dict()
		self.search_array = PriorityQueue()
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
		if self.path == self.map_copy.map_array:
			print("null")
		else:
			print("path:")
			self.print_map(self.path)
		print("#visits:")
		self.print_map(self.visits)
		print("first visit:")
		self.print_map(self.first_visit)
		print("last visit:")
		self.print_map(self.last_visit)

	def print_release(self):
		if self.path == self.map_copy.map_array:
			print("null")
		else:
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

		if child_node is not None:
			child_node.path_set = node_parent.path_set.copy()
			child_node.path_set.add(position)

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
			if direction not in node_parent.path_set:
				child_node = self.get_child_node(node_parent, direction)
				if (child_node is not None):
					child_arr.append(child_node)
		
		return(child_arr)

	def parse_path(self, node):
		for path_node in node.path_set:
			self.path[path_node[0]][path_node[1]] = "*"

	def get_cost(self, node_from, node_to):
		base_cost = 1
		if node_to.node.elevation > node_from.node.elevation:
			base_cost += (node_to.node.elevation - node_from.node.elevation)
		return (base_cost)


class MapInputError(Exception):
	pass


def exit_program(message):
	print(message)
	sys.exit(1) 