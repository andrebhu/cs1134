def list_min(lst, low, high):
	if low == high:
		return lst[low]

	else:
		min_val = list_min(lst, low + 1, high)
		if min_val > lst[low]:
			min_val = lst[low]
		return min_val
