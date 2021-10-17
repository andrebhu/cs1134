from ArrayStack import ArrayStack

class MaxStack:
	def __init__(self):
		self.data = ArrayStack()
		self.maximum = None

	def is_empty(self):
		if len(self.data) == 0:
			return True
		return False

	def __len__(self):
		return len(self.data)

	def push(self, e):
		self.data.push((e, self.maximum))
		if self.maximum == None or e > self.maximum:
			self.maximum = e		

	def top(self):
		if len(self.data) == 0:
			raise Exception("MaxStack is empty")
		return self.data.top()[0]

	def pop(self):
		if len(self.data) == 0:
			raise Exception("MaxStack is empty")

		a = self.data.pop()
		if a[1] == None or a[0] > a[1]:
			self.maximum = a[1]
		return a[0]

	def max(self):
		if len(self.data) == 0:
			raise Exception("MaxStack is empty")
		return self.maximum
'''
maxS = MaxStack()
maxS.push(3)
maxS.push(1)
maxS.push(6)
maxS.push(4)
print(maxS.max())
print(maxS.pop())
print(maxS.pop())
print(maxS.max())
'''