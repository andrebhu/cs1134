def two_sum(srt_lst, target):
	for i in range(len(srt_lst)):
		for j in range(i, len(srt_lst)):
			if srt_lst[i] + srt_lst[j] == target:
				return (i, j)
	return None

'''
a = [-2, 7, 11, 15, 20, 21]
print(two_sum(a, 22))
'''