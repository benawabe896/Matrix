def triangular_solve(rowlist, b):
	x = zero_vec(rowlist[0].D)
	for i in reversed(range(len(rowlist))):
		x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
	return x
