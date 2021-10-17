lst = [pow(-2, i) for i in range(8)]
lst = ["1" * i for i in range(1, 8)]

my_str = "Python"
#print([c for c in my_str*2])


#1
import copy
class Polynomial:
	def __init__(self, data=[0]):
		self.data = data

	def __add__(self, other):
		a = copy.deepcopy(self.data)
		b = copy.deepcopy(other.data)
		if len(a) != len(b):
			while len(a) < len(b):
				a.append(0)
			while len(b) < len(a):
				b.append(0)
		c = []
		for i in range(len(a)):
			c.append(a[i] + b[i])
		return Polynomial(c)

	def __call__(self, n):
		s = 0
		for i in range(len(self.data)):
			s += self.data[i] * pow(n, i)
		return s

	def __repr__(self):
		s = ""
		d = self.data[::-1]
		for i in range(len(self.data)):
			s += d[i] + "x^" + str(i)
			s += " + "
		return s

	def __mul__(self, other):
		pass


'''
poly1 = Polynomial([3, 7, 0, -9, 2])
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
poly3 = poly1 + poly2
print(poly3.data)

val1 = poly1(1)
print(val1)
val2 = poly2(1)
print(val2)
val3 = poly3(1)
print(val3)
'''

#2
class UnsignedBinaryInteger:
	def __init__(self, bin_num_str):
		self.data = bin_num_str

	def __add__(self, other):
		s = int("0b" + self.data, 2) + int("0b" + other.data, 2)
		return UnsignedBinaryInteger(bin(s)[2:])

	def decimal(self):
		return int("0b" + self.data, 2)

	def __lt__(self, other):
		if int("0b" + self.data, 2) < int("0b" + other.data, 2):
			return True
		return False

	def __gt__(self, other):
		if int("0b" + self.data, 2) > int("0b" + other.data, 2):
			return True
		return False

	def __eq__(self, other):
		if int("0b" + self.data, 2) == int("0b" + other.data, 2):
			return True
		return False

	def is_twos_power(self):
		if self.data.count("1") == 1:
			return True
		return False

	def largest_twos_power(self):
		return pow(2, len(self.data) - 1)

	def __repr__(self):
		return "0b" + self.data

b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("b1 is: ", b1)
print("b2 is: ", b2)

b3 = b1 + b2
print("b3 is: ", b3)
print("\nChecking decimal values:\n")
print(b1.decimal())
print(b2.decimal())
print(b3.decimal())

print("\nChecking comparisons:\n")
print(b1 < b2)
print(b2 < b1)
print(b1 > b2)
print(b2 > b1)
print(b1 + b2 == b3)

print("\nChecking is_twos_power:\n")
print(b1.is_twos_power())
print(b2.is_twos_power())
print(b3.is_twos_power())

print("\nChecking largest_twos_power:\n")
print(b1.largest_twos_power())
print(b2.largest_twos_power())
print(b3.largest_twos_power())