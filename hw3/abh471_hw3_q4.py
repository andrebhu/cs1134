def remove_all(lst, value):
		count = 0
		for i in range(len(lst)):
			if lst[i] == value:
				count += 1
			else:
				lst[i - count] = lst[i]

		for i in range(count):
			lst.pop()
