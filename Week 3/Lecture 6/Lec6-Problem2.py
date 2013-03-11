def oddTuples(aTup):
	divisors = () # the empty tuple
	count = 1

	if not aTup:
		return divisors
	else:
		for i in aTup:
			if count%2 != 0:
				divisors = divisors + (i,)
			count += 1
		
		return divisors	
	

print(oddTuples(()))
