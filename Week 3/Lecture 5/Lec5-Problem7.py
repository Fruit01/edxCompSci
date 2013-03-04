def lenRecur(aStr):
	print(aStr)
	if aStr == '':
		return 0
	else:
		return 1 + lenRecur(aStr[0:-1])


print(lenRecur('rocks'))