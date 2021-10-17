class StarRatings:
	def __init__(self, name=""):
		self.name = name
		self.data = []

	def giveRating(self, n):
		if n < 1 or n > 5:
			pass
		else:
			self.data.append(n)

	def calcAverage(self):
		total = 0
		length = 0
		for i in self.data:
			total += i
			length += 1
		return total/length

	def getStarCount(self):
		stars = [0, 0, 0, 0, 0]
		for i in self.data:
			stars[i - 1] += 1
		return stars

	def __add__(self, other):
		r = StarRatings()
		r.data.extend(self.data)
		r.data.extend(other.data)
		return r

	def __mul__(self, n):
		for i in range(len(self.data)):
			val = round(self.data[i] * n)
			if val > 5:
				self.data[i] = 5
			elif val < 1:
				self.data[i] = 1
			else:
				self.data[i] = int(val)
