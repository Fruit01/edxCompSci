aList = range(1, 6)
bList = aList
aList[2] = 'hello'
aList == bList

cList = range(6, 1, -1)
dList = []
for num in cList:
        dList.append(num)
cList == dList


cList is dList

cList[2] = 20
print(cList)