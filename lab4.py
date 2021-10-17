#1
def is_palindrome(s):
	for i in range(len(s)//2):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True
#print(is_palindrome("1racecar1"))

#2
def reverse_vowels(input_str):
	vowels = ["a", "e", "i", "o", "u"]
	
	input_vowels = []
	index = []
	a = list(input_str)
	for i in range(len(input_str)):
		if input_str[i] in vowels:
			input_vowels.append(input_str[i])
			index.append(i)

	index = index[::-1]
	for i in range(len(input_vowels)):
		a[index[i]] = input_vowels[i]
	return ''.join(a)

#print(reverse_vowels("tandon"))

#3
def shift_binary_search(lst, val):
	shift = 0
	for i in range(len(lst) - 1):
		if lst[i] > lst[i + 1]:
			shift = i + 1
			break
	
	

def find_shift(lst):
	for i in range(len(lst) - 1):
		if lst[i] > lst[i + 1]:
			return i + 1
lst = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
print(find_shift(lst))
