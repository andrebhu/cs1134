def shift(lst, k, d="left"):
	if d == "left":
		for i in range(k):
			lst.append(lst[0])
			lst.pop(0)
	elif d == "right":
		for i in range(k):
			lst.insert(0, lst[len(lst) - 1])
			lst.pop(len(lst) - 1)
'''
a = [1, 2, 3, 4, 5, 6]
shift(a, 2)
print(a)
shift(a, 2, "right")
print(a)
'''