def appearances(s, low, high):
	if low > high:
		return {}
	dict = appearances(s, low + 1, high)
	if s[low] in dict:
		dict[s[low]] += 1
		return dict
	else:
		dict[s[low]] = 1
		return dict

#print(appearances("Hello world", 0, len("Hello world") - 1))

