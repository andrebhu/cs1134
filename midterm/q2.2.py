def fast_closest_pair(lst):
	lst = sorted(lst)
	a, b = lst[0], lst[1]
	diff = abs(a - b)

	for i in range(1, len(lst) - 1):
		if abs(lst[i] - lst[i + 1]) < diff:
			a, b = lst[i], lst[i + 1]
	return a, b

'''
print(fast_closest_pair([3, 6, 4, 10, 23]))
print(fast_closest_pair([10, 45, 55, 42, 20]))
print(fast_closest_pair([4, 10, 6, 7, 10, 5]))
'''