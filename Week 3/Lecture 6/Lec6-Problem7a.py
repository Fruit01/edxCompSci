def applyToEach(L, f):
	for i in range(len(L)):
		L[i] = f(L[i])


testList = [1, -4, 8, -9]


def add_one(a):
    return a + 1

applyToEach(testList, add_one)

print testList