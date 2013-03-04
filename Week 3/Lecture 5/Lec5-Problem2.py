def recurPower(base, exp):
  '''
  base: int or float.
  exp: int >= 0

  returns: int or float, base^exp
  '''
  # Your code here
	if exp == 1:
    return base
  elif exp == 0:
  	return 1.0
  else:
    return base * recurPower(base, exp-1)
