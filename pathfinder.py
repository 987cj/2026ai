import sys
import utils
from readmap import read_map

mode = -1
algorithm = -1
heuristic = -1

# Handle command line arguments
if (sys.argv.__len__() != 5):
	utils.exit_program("Not enough arguments: python pathfinder.py [mode] [map] [algorithm] [heuristic]")

match sys.argv[1]:
	case "debug":
		mode = 0
	case "release":
		mode = 1
	case _:
		utils.exit_program("Invalid mode: mode types are debug, release")

map = read_map(sys.argv[2])

#algorithm
match sys.argv[3]:
	case "bfs":
		algorithm = 0
	case "ucs":
		algorithm = 1
	case "astar":
		algorithm = 2
	case _:
		utils.exit_program("Invalid algorithm: algorithm types are bfs, ucs, astar.")

match sys.argv[4]:
	case "euclidean":
		heuristic = 0
	case "manhattan":
		heuristic = 1
	case _:
		utils.exit_program("Invalid heuristic: heuristic types are euclidean, manhattan")