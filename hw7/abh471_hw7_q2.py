from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
	new = BinarySearchTreeMap()
	for i in range(n):
		new.insert(i + 1)
	return new
'''
a = create_chain_bst(4).root
while a != None:
	print(a.item.key)
	a = a.right
'''

def create_complete_bst(n):
	bst = BinarySearchTreeMap()
	add_items(bst, 1, n)
	return bst

def add_items(bst, low, high):
	mid = (low + high) // 2
	bst.insert(mid)
	if low != high:
		add_items(bst, low, mid - 1)
		add_items(bst, mid + 1, high)
'''
a = create_complete_bst(7).root
print(a.item.key)
print(a.left.item.key, a.right.item.key)
print(a.left.left.item.key, a.left.right.item.key, a.right.left.item.key, a.right.right.item.key)
'''

