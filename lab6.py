#1
def sum_to(n):
	if n == 1:
		return 1
	else:
		return n + sum_to(n - 1)

#2
def product_evens(n):
	if n == 2:
		return 2
	else:
		if n % 2 == 1:
			return product_evens(n - 1)
		else:
			return n * product_evens(n - 2)

#3
def find_max(lst, low, high):
	if len(lst) == 1:
		return lst[0]

	prev = find_max(lst[low:high + 1], 1, high)

	if prev > lst[low]:
		return prev
	return lst[low]

#print(find_max([13, 9, 16, 3, 4, 2], 0, 5))

#4
def is_palindrome(input_str, low, high):
	if len(input_str) <= 2 and input_str[low:] == input_str[:high]:
		return True

	if input_str[low] != input_str[high]:
		return False
	else:
		return is_palindrome(input_str[low + 1: high], 0, -1)

#print(is_palindrome("racecar", 0, 6))
#print(is_palindrome("racecar", 1, 5))
#print(is_palindrome("racecar", 1, 3))

#5
def binary_search(lst, low, high, val):
	print(lst, low, high, val)

	if low == high and len(lst) == 1:
		return low
	elif low != high and len(lst) == 1:
		return None

	if lst[(high - low) // 2] == val:
		return (high - low) // 2

	print("Looking at " + str(lst[(high - low) // 2]))
	if lst[(high - low) // 2] < val:
		low = (high - low) // 2
		
	elif lst[(high - low) // 2] > val:
		high = (high - low) // 2
		
	return binary_search(lst[low:high], 0, len(lst[low:high]), val)

print(binary_search([0, 1, 2, 3, 4, 5, 6, 7], 0, 8, 4))


#6



