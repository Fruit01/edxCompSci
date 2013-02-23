def isVowel2(char):
	'''
	char: a single letter of any case

	returns: True if char is a vowel and False otherwise.
	'''
	# Your code here
	vowels = ('a','e','i','o','u','A','E','I','O','U')
	final = False

	for vowel in vowels:
		if(char == vowel):
			final = True
	return final

print(isVowel2('o'))


# MIT Version, much better than mine :print

def isVowelMIT(char):
	'''
	char: a single letter of any case

	returns: True if char is a vowel and False otherwise.
	'''
	if char in 'aeiouAEIOU':
	    return True
	else:
	    return False