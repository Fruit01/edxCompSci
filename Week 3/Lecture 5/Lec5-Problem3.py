def recurPowerNew(base, exp):

	if exp > 0 and exp %2 == 0:
		newbase = base * base
		newexp = exp / 2 
		return recurPowerNew(newbase, newexp)

	if exp > 0 and exp %2 != 0:
		return base * recurPowerNew(base, exp-1)
		
	if exp == 0:
		return 1

print(recurPowerNew(2, 5))
print(2**5);


