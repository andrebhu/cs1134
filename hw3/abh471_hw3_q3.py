def find_duplicates(lst):
	count = [0 for i in range(len(lst))]
	duplicates = []
	for i in lst:
		count[i] += 1
	for i in range(len(count)):
		if count[i] > 1:
			duplicates.append(i)
	return duplicates


lst = [2, 4, 4, 1, 2]
print(find_duplicates(lst))
