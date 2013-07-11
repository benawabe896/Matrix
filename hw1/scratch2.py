def triangular_solve(rowlist, label_list, b):
	x = zero_vec(set(label_list))
	for r in reversed(range(len(rowlist))):
		c = label_list[r]
		x[c] = (b[r] - x*rowlist[r])/rowlist[r][c]
	return x
