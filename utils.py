import sys

class Map:
	size = (0, 0)
	start = (0, 0)
	end = (0, 0)
	map =[[]]

def exit_program(message):
	print(message)
	sys.exit(1) 