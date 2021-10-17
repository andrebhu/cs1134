class Vector:
	#part a
	def __init__(self, d):
		if isinstance(d, list):
			self.coords = d
		elif isinstance(d, int):
			self.coords = [0] * d

	def __len__(self):
		return len(self.coords)

	def __getitem__(self, j):
		return self.coords[j]

	def __setitem__(self, j, val):
		self.coords[j] = val

	def __add__(self, other):
		if (len(self) != len(other)):
			raise ValueError("dimensions must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		return self.coords == other.coords

	def __ne__(self, other):
		return not (self == other)

	def __str__(self):
		return '<' + str(self.coords)[1:-1] + '>'

	def __repr__(self):
		return str(self)

#part b
	def __sub__(self, other):
		if len(self) != len(other):
			raise ValueError("dimensions must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result

#part c
	def __neg__(self):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] * -1
		return result

#part d, f
	def __mul__(self, other):
		result = Vector(len(self))

		#scalar product
		if isinstance(other, int):
			for j in range(len(self)):
				result[j] = self[j] * other
			return result	

		#dot product
		if len(self) != len(other):
			raise ValueError("dimensions must agree")
		elif isinstance(other, Vector):
			p = 0
			for j in range(len(self)):
				p += self[j] * other[j]
			return p

#part e
	def __rmul__(self, other):
		result = Vector(len(self))
		if isinstance(other, int):
			for j in range(len(self)):
				result[j] = self[j] * other
			return result

v1 = Vector(5)
v1[1] = 10
v1[-1] = 10
print(v1)

v2 = Vector([2, 4, 6, 8, 10])
print(v2)

u1 = v1 + v2
print(u1)

u2 = -v2
print(u2)

u3 = 3 * v2
print(u3)

u4 = v2 * 3
print(u4)

u5 = v1 * v2
print(u5)
