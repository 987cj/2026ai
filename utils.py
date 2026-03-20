import sys


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
		self.parent = None

class MapInputError(Exception):
	pass


def exit_program(message):
	print(message)
	sys.exit(1) 