from DoublyLinkedList import DoublyLinkedList

class Integer:
	def __init__(self, num_str):
		self.data = DoublyLinkedList()
		for i in num_str:
			self.data.add_last(int(i))

	def __add__(self, other):
		a = Integer("")
		carry = 0
		s1 = self.data.trailer
		s2 = other.data.trailer

		while s1.prev.data is not None and s2.prev.data is not None:
			result = s1.prev.data + s2.prev.data + carry
			a.data.add_first(result % 10)
			carry = result // 10
			s1, s2 = s1.prev, s2.prev

		while s1.prev.data is not None:
			result = s1.prev.data + carry
			a.data.add_first(result % 10)
			carry = result // 10
			s1 = s1.prev

		while s2.prev.data is not None:
			result = s2.prev.data + carry
			a.data.add_first(result % 10)
			carry = result // 10
			s2 = s2.prev

		if carry != 0:
			a.data.add_first(carry)

		while a.data.header.next.data == 0:
			a.data.delete_first()

		return a

	def __repr__(self):
		strings_lst = [str(elem) for elem in self.data]
		return "".join(strings_lst)

'''
n1 = Integer('007')
n2 = Integer('20')
n3 = n1 + n2
print(n3)
'''