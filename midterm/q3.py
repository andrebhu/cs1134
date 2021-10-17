def two_sort(lst):
	count = 0
	val1 = lst[0]
	val2 = None

	for i in range(len(lst)):
		if lst[i] != val1:
			count += 1
			val2 = lst[i]
			lst[i] = val1			

	for i in range(count):
		lst.pop()

	for i in range(count):
		lst.append(val2)

a = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
two_sort(a)
print(a)