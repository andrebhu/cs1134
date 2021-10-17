def find_min(lst):
	if len(lst) == 1:
		return lst[0]
	else:
		m = find_min(lst[1:])
		n = lst[0]
		if m < n:
			n = m
		return n

a = [13, 9, 16, 3, 4, 2]
print(find_min(a))


def recurse(min1, min2, list):
    if len(list)==0:
        return min2
    first, rest = list[0], list[1:]
    if first < min1:
        return recurse(first, min1, rest)
    if first < min2:
        return recurse(min1, first, rest)
    return recurse(min1, min2, rest)

def second_smallest(list):
    if len(list) < 2:
        raise ValueError("too few elements to find second_smallest")
    a, b, rest = list[0], list[1], list[2:]
    if b < a:
        return recurse(b, a, rest)
    else:
        return recurse(a, b, rest)
print(second_smallest(a))