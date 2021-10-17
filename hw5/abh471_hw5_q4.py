from ArrayStack import ArrayStack

class Queue:
	def __init__(self):
		self.s1 = ArrayStack()
		self.s2 = ArrayStack()

	def is_empty(self):
		if self.s1.is_empty():
			return True
		return False

	def __len__(self):
		return len(self.s1)

	def enqueue(self, e):
		self.s1.push(e)

	def first(self):
		return self.s1.top()

	def dequeue(self):
		while len(self.s1) != 0:
			self.s2.push(self.s1.pop())
		r = self.s2.pop()
		while len(self.s2) != 0:
			self.s1.push(self.s2.pop())
		return r
'''
q = Queue()
for i in range(10):
	q.enqueue(i)
while q.is_empty() == False:
	print(q.dequeue())
'''