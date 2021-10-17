from BinarySearchTreeMap import BinarySearchTreeMap

a = BinarySearchTreeMap()
for i in [1, 2, 3, 5, 12, 9, 21, 19, 25]:
	a.insert(i)

def min_max_BST(bst):
	inorder = bst.inorder()
	minimum = next(inorder).item.key
	maximum = None
	for i in inorder:
		maximum = i.item.key
	return (minimum, maximum)

print(min_max_BST(a))

def glt_n(bst, n):
	inorder = bst.inorder()
	temp = None
	for i in inorder:
		if i.item.key == n:
			return n
		else:
			if i.item.key > n:
				return temp
			else:
				temp = i.item.key

print(glt_n(a, 21))
print(glt_n(a, 4))

a = BinarySearchTreeMap()
for i in [5, 10, 12, 15, 20, 25]:
	a.insert(i)

b = BinarySearchTreeMap()
for i in [5, 10, 12, 15, 20, 25]:
	b.insert(i)

def compare_BST(bst1, bst2):
	inorder_1 = bst1.inorder()
	inorder_2 = bst2.inorder()
	for i in inorder_1:
		if i.item.key != next(inorder_2).item.key:
			return False
	return True

print(compare_BST(a, b))