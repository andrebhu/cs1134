#Runtime: O(n)
def __sub__(self, other):
		r = DoublyLinkedList()
		s_node = self.header.next
		o_node = other.header.next

		while s_node.data != None and o_node.data != None:
			s = s_node.data
			o = o_node.data
			if s == o:
				s_node = s_node.next
				o_node = o_node.next
			elif s != o:
				if s > o:
					o_node = o_node.next
				elif s < o:
					r.add_last(s)
					s_node = s_node.next

		#add remaining self
		while s_node.data != None:
			s = s_node.data
			r.add_last(s)
			s_node = s_node.next

		return r