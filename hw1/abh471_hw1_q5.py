def fibs(n):
	a = 0
	b = 1
	count = 0
	while count < n:
		yield b
		a, b = b, a + b
		count += 1

'''
for curr in fibs(8):
	print(curr)
'''