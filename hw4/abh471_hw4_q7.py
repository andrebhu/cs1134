def split_by_sign(lst, low, high):
	if low == high:
		return None
	if lst[low] < 0:
		split_by_sign(lst, low + 1, high)
	elif lst[low] > 0:
		for i in range(low, high):
			lst[i], lst[i + 1] = lst[i + 1], lst[i]
		split_by_sign(lst, low, high - 1)