from DoublyLinkedList import DoublyLinkedList
import copy

def copy_linked_list(lnk_lst):
	c = DoublyLinkedList()
	for i in lnk_lst:
			c.add_last(copy.copy(i))
	return c

def deep_copy_linked_list(lnk_lst):
	c = DoublyLinkedList()
	for i in lnk_lst:
		if isinstance(i, int):
			c.add_last(copy.deepcopy(i))
		else:
			c.add_last(copy.deepcopy(deep_copy_linked_list(i)))
	return c
'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
print(elem1)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)

lnk_lst2 = copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10

e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
'''
'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)

lnk_lst2 = deep_copy_linked_list(lnk_lst1)

e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10

e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
'''