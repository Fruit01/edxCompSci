def clip(lo, x, hi):
	'''
	Takes in three numbers and returns a value based on the value of x.
	Returns:
	- lo, when x < lo
	- hi, when x > hi
	- x, otherwise
	'''
	return(max(lo, min(hi, x)))

print(clip(-7.31, -0.79, 3.3))