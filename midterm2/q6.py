from DoublyLinkedList import DoublyLinkedList
#NO PREV

def odd_even_sorter(head):
	node1 = head.next
	while node1.data != None:
		node2 = node1.next
		while node2.data != None:
			if node1.data % 2 == 0 and node2.data % 2 == 1:
				node1.data, node2.data = node2.data, node1.data
			node2 = node2.next
		node1 = node1.next
'''
a = DoublyLinkedList()
b = DoublyLinkedList()
c = [1, 2, 3, 4]
for i in c:
	a.add_last(i)
odd_even_sorter(a.header)
print(a)

c = [53, 97, 7, 52, 36, 20, 90]
for i in c:
	b.add_last(i)
odd_even_sorter(b.header)
print(b)
'''