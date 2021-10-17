#Runtime: n log n

def sum_exists(ls, val):
	ls = sorted(ls)
	a, b = 0, len(ls) - 1
	while a < b:
		if ls[a] + ls[b] == val:
			return True
		else:
			if ls[a] + ls[b] < val:
				a += 1
			else:
				b -= 1
	return False
'''
print(sum_exists([8, 4, 6, 1], 10))
print(sum_exists([1, 2, 3, 4, 5], 90))
print(sum_exists([3, 7, 2, 9, 1, 4], 10))
print(sum_exists([1, 2, 2, 3, 4, 5, 6], 4))
'''
