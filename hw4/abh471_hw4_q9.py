def permutations(lst, low, high):
	if low == high:
		return [[lst[low]]]	
	
	ret_list = []

	for i in range(high - low + 1):
		for j in permutations(lst, low + 1, high):
			j.insert(i, lst[low])
			ret_list.append(j)

	return ret_list

#print(permutations([1, 2, 3], 0, 2))