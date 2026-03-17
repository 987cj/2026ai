import utils
import traceback


def read_map(mapfile):
	try:
		file = open(mapfile, "r")
		size_text = file.readline().split()
		if (len(size_text) != 2):
			raise(utils.MapInputError)
		start_text = file.readline()
		print(size_text, start_text)
		file.close()
	except FileNotFoundError:
		utils.exit_program("File not found.")
	except utils.MapInputError:
		utils.exit_program("Map File is not configured correctly.")
	except Exception:
		traceback.print_exc()
		utils.exit_program("Error Occurred.")