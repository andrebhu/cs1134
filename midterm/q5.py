def remove_indices(lst, remove):
	count = 0
	for i in range(len(lst)):
		if i == remove[count]:
			count += 1
		else:
			lst[i - count] = lst[i]

	for i in range(count):
		lst.pop()
'''
def main():
	full_list = [10, 20, 30, 40, 50]
	index_list = [1, 4]
	remove_indices(full_list, index_list)
	print(full_list)
main()
'''