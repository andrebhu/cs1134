from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):

	def merge_sublists(s1, s2, srt_lnk_lst1, srt_lnk_lst2):
		if s1.data == None and s2.data != None:
			n = DoublyLinkedList()
			while s2.data is not None:
				n.add_last(s2.data)
				s2 = s2.next

		elif s1.data != None and s2.data == None:
			n = DoublyLinkedList()
			while s1.data != None:
				n.add_last(s1.data)
				s1 = s1.next
		else:
			if s1.data > s2.data:
				n = merge_sublists(s1, s2.next, srt_lnk_lst1, srt_lnk_lst2)
				n.add_first(s2.data)
			else:
				n = merge_sublists(s1.next, s2, srt_lnk_lst1, srt_lnk_lst2)
				n.add_first(s1.data)
		return n


	s1 = srt_lnk_lst1.header.next
	s2 = srt_lnk_lst2.header.next
	return merge_sublists(s1, s2, srt_lnk_lst1, srt_lnk_lst2)


'''
srt_lnk_lst1 = DoublyLinkedList()
a = [1, 3, 5, 6, 8]
for i in a:
	srt_lnk_lst1.add_last(i)
srt_lnk_lst2 = DoublyLinkedList()
a = [2, 3, 5, 10, 15, 18]
for i in a:
	srt_lnk_lst2.add_last(i)

print(merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2))
'''