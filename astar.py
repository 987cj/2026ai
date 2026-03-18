import utils

class AStar(utils.MapAlgorithm):
	def __init__(self, path_map, heuristic):
		self.map_copy = path_map
		self.heuristic = heuristic
		self.path = copy.deepcopy(path_map.map_array)
		self.visits = self._MapAlgorithm__create_empty_map()
		self.visits_index = 0
		self.first_visit = self._MapAlgorithm__create_empty_map()
		self.last_visit = self._MapAlgorithm__create_empty_map()
		self.map_nodes = dict()
		self.__create_nodes()