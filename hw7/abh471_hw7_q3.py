from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
	bst = BinarySearchTreeMap()
	if len(prefix_lst) == 0:
		return bst
	elif len(prefix_lst) == 1:
		bst.insert(prefix_lst[0])
		return bst
	else:
		for i in prefix_lst:
			bst.insert(i, i)
	return bst
'''
a = restore_bst([9, 7, 3, 1, 5, 13, 11, 15]).root
print(a.item.key)
print(a.left.item.key, a.right.item.key)
print(a.left.left.item.key, a.right.left.item.key, a.right.right.item.key)
print(a.left.left.left.item.key, a.left.left.right.item.key)
'''