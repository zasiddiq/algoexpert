def firstDuplicateValue(array):
	
	if len(array) == 0 or len(array) == 1:
		return -1

	setOfNumbers = set()
	for i in array:
		if i not in setOfNumbers:
			setOfNumbers.add(i)
		else:
			return i
	return -1
		
	
	return []