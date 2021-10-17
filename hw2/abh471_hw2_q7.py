def findChange(lst01):
	low = 0
	high = len(lst01) - 1
	mid = (high + low) // 2

	while lst01[mid] != 1 or lst01[mid - 1] != 0:
		if lst01[mid] == 0:
			low = mid + 1
		else:
			high = mid

		mid = (high + low) // 2
	return mid

'''
lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
lst01 = [0, 0, 1]
lst01 = [0, 1]
lst01 = [0, 1, 1, 1, 1]
lst01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
print(findChange(lst01))
'''