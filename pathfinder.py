import sys
import utils
from readmap import read_map
from bfs import BFS

heuristic = -1
search = None

# Handle command line arguments
if not (len(sys.argv) == 4 or len(sys.argv) == 5):
	utils.exit_program("Incorrect number of arguments: python pathfinder.py [mode] [map] [algorithm] [heuristic]")

if not(sys.argv[1] == "debug" or sys.argv[1] == "release"):
	utils.exit_program("Invalid mode: mode types are debug, release")

path_map = read_map(sys.argv[2])

#algorithm
match sys.argv[3]:
	case "bfs":
		search = BFS(path_map)
	case "ucs":
		pass
	case "astar":
		if len(sys.argv) != 5:
			utils.exit_program("Incorrect number of arguments: python pathfinder.py [mode] [map] [algorithm] [heuristic]")
		match sys.argv[4]:
			case "euclidean":
				heuristic = 0
			case "manhattan":
				heuristic = 1
			case _:
				utils.exit_program("Invalid heuristic: heuristic types are euclidean, manhattan")
	case _:
		utils.exit_program("Invalid algorithm: algorithm types are bfs, ucs, astar.")

search.search()

match sys.argv[1]:
	case "debug":
		search.print_debug()
	case "release":
		search.print_release()
	case _:
		utils.exit_program("Invalid mode: mode types are debug, release")
