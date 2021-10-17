def split_parity(lst):
	i = 0
	evens = 0

	while i + evens < len(lst):
		if lst[i] % 2 == 0:
			lst.append(lst.pop(i))
			evens += 1

		elif lst[i] % 2 == 1:
			i += 1

	return lst

'''
a = [1, 2, 3, 4]
split_parity(a)
print(a)
'''