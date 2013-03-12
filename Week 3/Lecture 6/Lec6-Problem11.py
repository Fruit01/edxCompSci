def biggest(animals):

  result = None
  biggestValue = 0
  for key in animals.keys():
  		if len(animals[key]) >= biggestValue:
  			result = key
  			biggestValue = len(animals[result])
  return result


# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: The key with the largest number of values associated with it
#     '''
#     result = None
#     biggestValue = 0
#     for key in aDict.keys():
#         if len(aDict[key]) >= biggestValue:
#             result = key
#             biggestValue = len(aDict[key])
#     return result

print(biggest({'a': [13, 7, 18, 8, 7, 20, 2, 14], 'c': [10, 4], 'b': [10, 10, 3, 15, 6, 1, 9], 'd': [10, 2, 13, 1, 5]}))