def gcdRecur(a, b):

	if b == 0:
		return a
	
	if(b != 0 and a != 0):
		return gcdRecur(b, a % b)
		



print(gcdRecur(9, 12))