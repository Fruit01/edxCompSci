def gcdIter(a, b):
	gdc = min(a,b)
	while gdc>0:
		if a%gdc == 0 and b%gdc == 0:
			break
		else:
			gdc -= 1
	return gdc

print(gcdIter(6, 12))