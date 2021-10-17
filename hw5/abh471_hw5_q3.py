from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
	def __init__(self):
		self.stack = ArrayStack()
		self.deque = ArrayDeque()

	def is_empty(self):
		if self.stack.is_empty() and self.deque.is_empty():
			return True
		return False

	def __len__(self):
		return len(self.stack) + len(self.deque)

	def push(self, e):
		self.deque.enqueue_last(e)
		if len(self.stack) < len(self.deque):
			self.stack.push(self.deque.dequeue_first())

	def top(self):
		if self.is_empty():
			raise Exception("MidStack is empty")
		if self.deque.is_empty():
			return self.stack.top()
		return self.deque.last()

	def pop(self):
		if self.is_empty():
			raise Exception("MidStack is empty")
		if len(self.stack) > len(self.deque):
			self.deque.enqueue_first(self.stack.pop())
		return self.deque.dequeue_last()

	def mid_push(self, e):
		if len(self.stack) > len(self.deque):
			self.deque.enqueue_first(e)
		else:
			self.stack.push(e)
'''
midS = MidStack()
midS.push(2)
midS.push(4)
midS.push(6)
midS.push(8)
midS.push(10)
midS.mid_push(12)
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
'''