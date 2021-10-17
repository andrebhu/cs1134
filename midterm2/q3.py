def max_digits(int_val):
	if int_val < 10:
		return int_val
	else:
		n = int_val % 10
		if n > max_digits(int_val // 10):
			return n
		else:
			return max_digits(int_val // 10)
'''
print(max_digits(123))
print(max_digits(2020))
print(max_digits(1724372))
'''