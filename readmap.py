import utils
import traceback


def read_map(mapfile):
	try:
		file = open(mapfile, "r")
		new_map =process_map_input(file)
		file.close()
	except FileNotFoundError:
		utils.exit_program("File not found.")
	except Exception:
		traceback.print_exc()
		utils.exit_program("Error Occurred.")
	return (new_map)


def process_map_input(file):
	new_map = utils.Map()
	size = process_line(file.readline(), 2)
	start_pos = process_line(file.readline(), 2)
	end_pos = process_line(file.readline(), 2)
	map_arr = []
	for i in range(size[0]):
		new_row = process_line(file.readline(), size[1])
		map_arr.append(new_row)
	new_map.size = (size[0], size[1])
	new_map.start = (start_pos[0], start_pos[1])
	new_map.end = (end_pos[0], end_pos[1])
	new_map.map = map_arr
	return(new_map)


def process_line(line, num_elements):
	line_text = line.split()
	try:
		if len(line_text) != 2:
			raise(utils.MapInputError)
		for i in range(len(line_text)):
			line_text[i] = int(line_text[i])
	except (utils.MapInputError, ValueError):
		utils.exit_program("Map File is not configured correctly.")
	except Exception:
		traceback.print_exc()
		utils.exit_program("Error Occurred.")
	return(line_text)

