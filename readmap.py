import utils
import traceback

def readmap(mapfile):
	try:
		file = open(mapfile, "r")
		sizetext = file.readline()
		starttext = file.readline()
		print(sizetext, starttext)
		file.close()
	except FileNotFoundError:
		utils.exit_program("File not found.")
	except Exception:
		traceback.print_exc()
		utils.exit_program("Error Occurred.")