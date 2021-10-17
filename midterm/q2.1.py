def closest_pair(lst):
	a, b = lst[0], lst[1]
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			if abs(a - b) > abs(lst[i] - lst[j]):
				a, b = lst[i], lst[j]
	return a, b
'''
print(closest_pair([3, 6, 4, 10, 23]))
print(closest_pair([10, 45, 55, 42, 20]))
print(closest_pair([4, 10, 6, 7, 10, 5]))
'''

