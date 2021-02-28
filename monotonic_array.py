def isMonotonic(array):
    
	if len(array) == 0 or len(array) == 1:
		return True
	
	if len(array) == 2:
		return True
	
	# check if same
	result = len(set(array))
	if result == 1:
		return True
	

	decreasing = False
	increasing = False

	start = array[0]
	nextNonSameVal = 1
	for i in array:
		if i == start:
			nextNonSameVal += 1
	second = array[nextNonSameVal]
	
	if start > second:
		decreasing = True
	
	if start < second:
		increasing = True
		
	
	if decreasing:
		
		current = array[0]
		for index, val in enumerate(array[1:]):
			current = array[index]
			if val > current:
				return False
		
		return True

	if increasing:
		current = array[0]
		for index, val in enumerate(array[1:]):
			current = array[index]
			if val < current:
				return False
		
		return True
		
		return True

array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
print (isMonotonic(array))