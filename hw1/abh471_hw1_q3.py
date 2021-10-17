#part a
def square_sum(n):
	s = 0
	for i in range(1, n):
		s += i*i
	return s

#part b
sum([i*i for i in range(1, 10)])

#part c
def odd_square_sum(n):
	s = 0
	for i in range(1, n):
		if i % 2 == 1:
			s += i*i
	return s
	
#part d
sum([i*i for i in range(1, 10) if i % 2 == 1])
