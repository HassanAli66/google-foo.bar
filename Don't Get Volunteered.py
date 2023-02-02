def solution(src, dest):
	moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
	if src == dest:
		return 0

	def check_neighbs(steps, cell_list):
		if dest in cell_list:
			return steps
		return check_neighbs(steps+1, get_neigbs(cell_list))

	def get_neigbs(cell_list):
		def c_to_num(x, y):
			return (x * 8) + y
		def valid(x, y):
			if x in range(8) and y in range(8):
				return True
			else:
				return False
		neighbs = []
		for cell in cell_list:
			x = cell % 8
			y = cell // 8
			for (j, k) in moves:
				cords = c_to_num(x+j, y+k)
				if valid(x+j, y+k) and cords not in neighbs:
					neighbs.append(cords)
		return neighbs

	return check_neighbs(1, get_neigbs([src]))

