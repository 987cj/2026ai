import sys


class PathMap:
	size = (0, 0)
	start = (0, 0)
	end = (0, 0)
	map_array =[[]]

class MapAlgorithm:
	def __init__(self, path_map):
		self.map_copy = path_map
		self.path = path_map.map_array
		self.visits = self._MapAlgorithm__create_empty_map()
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.nodes = dict()
	
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

class MapInputError(Exception):
	pass


def exit_program(message):
	print(message)
	sys.exit(1) 