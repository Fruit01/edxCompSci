def iterPower(base, exp):
  '''
  base: int or float.
  exp: int >= 0

  returns: int or float, base^exp
  '''
  # Your code here
  result = 1
  for turn in range(exp):
      result = result * base
  return result

print(iterPower(2,5))
print(2**5)