from DoublyLinkedList import DoublyLinkedList

class CompactString:
	def __init__(self, orig_str):
		self.data = DoublyLinkedList()
		if len(orig_str) == 0:
			return
		c = orig_str[0]
		n = 0
		for char in orig_str:
			if char == c:
				n += 1
			else:
				self.data.add_last((c, n))
				c = char
				n = 1
		self.data.add_last((c, n))

	def __add__(self, other):
		s = CompactString("")

		s1 = self.data.header
		s2 = other.data.header

		while s1.next.next.data != None:
			s.data.add_last(s1.next.data)
			s1 = s1.next
		s1 = s1.next

		if s1.data[0] == s2.next.data[0]:
			n = s1.data[1] + s2.next.data[1]
			s.data.add_last((s1.data[0], n))
			s2 = s2.next
		s2 = s2.next

		while s2.next.data != None:
			s.data.add_last(s2.data)
			s2 = s2.next
		s.data.add_last(s2.data)
		return s


	def __lt__(self, other):
		s1 = self.data.header.next
		s2 = other.data.header.next

		while s1.data == s2.data:
			s1 = s1.next
			s2 = s2.next

		if s1.data == None and s2.data == None:
			return False
		elif s1.data != None and s2.data == None:
			return False
		elif s1.data == None and s2.data != None:
			return False
		else:
			if s1.data[0] == s2.data[0]:
				if s1.data[1] > s2.data[1]:
					if s2.next.data == None:
						return False
					return s1.data[0] < s2.next.data[0]
				else:
					if s1.next.data == None:
						return True
					return s1.next.data[0] < s2.data[0]
			else:
				return s1.data[0] < s2.data[0]

	def __le__(self, other):
		s1 = self.data.header.next
		s2 = other.data.header.next

		while s1.data == s2.data:
			s1 = s1.next
			s2 = s2.next

		if s1.data == None and s2.data == None:
			return True
		elif s1.data != None and s2.data == None:
			return False
		elif s1.data == None and s2.data != None:
			return True
		else:
			if s1.data[0] == s2.data[0]:
				if s1.data[1] > s2.data[1]:
					if s2.next.data == None:
						return False
					return s1.data[0] < s2.next.data[0]
				else:
					if s1.next.data == None:
						return True
					return s1.next.data[0] < s2.data[0]
			else:
				return s1.data[0] < s2.data[0]

	def __gt__(self, other):
		s1 = self.data.header.next
		s2 = other.data.header.next

		while s1.data == s2.data:
			s1 = s1.next
			s2 = s2.next

		if s1.data == None and s2.data == None:
			return False
		elif s1.data != None and s2.data == None:
			return True
		elif s1.data == None and s2.data != None:
			return False
		else:
			if s1.data[0] == s2.data[0]:
				if s1.data[1] > s2.data[1]:
					if s2.next.data == None:
						return True
					return s1.data[0] > s2.next.data[0]
				else:
					if s1.next.data == None:
						return False
					return s1.next.data[0] > s2.data[0]
			else:
				return s1.data[0] > s2.data[0]

	def __gt__(self, other):
		s1 = self.data.header.next
		s2 = other.data.header.next

		while s1.data == s2.data:
			s1 = s1.next
			s2 = s2.next

		if s1.data == None and s2.data == None:
			return True
		elif s1.data != None and s2.data == None:
			return True
		elif s1.data == None and s2.data != None:
			return False
		else:
			if s1.data[0] == s2.data[0]:
				if s1.data[1] > s2.data[1]:
					if s2.next.data == None:
						return True
					return s1.data[0] > s2.next.data[0]
				else:
					if s1.next.data == None:
						return False
					return s1.next.data[0] > s2.data[0]
			else:
				return s1.data[0] > s2.data[0]

	def __repr__(self):
		return str(self.data)