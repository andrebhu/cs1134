def add_binary(bin_num1, bin_num2):
	a, b = 0, 0
	for i in range(len(bin_num1)):
		if bin_num1[::-1][i:i+1] == "1":
			a += pow(2, i)
	for i in range(len(bin_num2)):
		if bin_num2[::-1][i:i+1] == "1":
			b += pow(2, i)
	c = a + b
	s = ""
	while c > 0:
		s += str(c % 2)
		c = c // 2
	return s[::-1]

#print(add_binary("11", "1"))

def can_construct(word, letters):
	l = letters
	for c in word:
		if c not in l:
			return False
		else:
			l = l.replace(c, "", 1)
	return True

#print(can_construct("apples", "aples"))
#print(can_construct("apples", "aplespl"))

class Complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __add__(self, other):
		return Complex(self.a + other.a, self.b + other.b)

	def __sub__(self, other):
		return Complex(self.a - other.a, self.b - other.b)

	def __mul__(self, other):
		return Complex((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))

	def __repr__(self):
		if self.b >= 0:
			return str(self.a) + " + " + str(self.b) + "i"
		elif self.b < 0:
			return str(self.a) + " - " + str(self.b)[1:] + "i"


#cplx1 = Complex(5, 2)
#print(cplx1)
#cplx2 = Complex(3, 3)
#print(cplx2)
#print(cplx1 + cplx2)
#print(cplx1 - cplx2)
#print(cplx1 * cplx2)
#print(cplx1)
#print(cplx2)

import random

def create_permutation(n):
	d = [x for x in range(n)]
	r = []
	while d:
		r.append(d.pop(random.randint(0, len(d) - 1)))
	return r

#print(create_permutation(6))

def scramble_word(word):
	order = create_permutation(len(word))
	s = ""
	for i in order:
		s += word[i]
	return s

#print(scramble_word("pokemon"))

def guessing_game(word):
	print("Unscramble the word: " + scramble_word(word))
	for i in range(1, 4):
		answer = input("Try #%s: " % i)
		if answer == word:
			print("Yay, you got it!")
			break
		else:
			print("Wrong!")


#guessing_game("pokemon")
