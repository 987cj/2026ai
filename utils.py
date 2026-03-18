import sys


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


class MapInputError(Exception):
	pass


def exit_program(message):
	print(message)
	sys.exit(1) 