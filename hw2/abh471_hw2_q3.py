import math

def factors(num):
	for i in range(1, int(math.sqrt(num))):
		if num % i == 0:
			yield i

	for i in range(int(math.sqrt(num)), 0, -1):
		if num % i == 0:
			yield num // i

'''
for curr_factor in factors(100):
	print(curr_factor, end=" ")
'''