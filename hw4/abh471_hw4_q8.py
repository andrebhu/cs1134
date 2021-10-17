def flat_list(nested_lst, low, high):
	if low > high:
		return nested_lst
	if isinstance(nested_lst[low], list):
		t = nested_lst.pop(low)
		for i in range(len(t)):
			nested_lst.insert(low + i, t[i])
		return flat_list(nested_lst, low, high + len(t) - 1)
	else:
		return flat_list(nested_lst, low + 1, high)


a = [[1, 2], 3, [4, [5, 6, [7], 8]]]
print(flat_list(a, 0, 2))


def new(s):
	if s == []:
		return s
	if isinstance(s[0], list):
		return new(s[0]) + new(s[1:])
	return s[:1] + new(s[1:])

print(new(a))