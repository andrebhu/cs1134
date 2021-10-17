from LinkedBinaryTree import LinkedBinaryTree

def bt_even_sum(root):
	if root is None:
		return 0
	else:
		left = bt_even_sum(root.left)
		right = bt_even_sum(root.right)
		if root.data % 2 == 0:
			return root.data + left + right


def bt_contains(root, val):
	if root.data == val:
		return True
	else:
		if root.left is not None:
			return bt_contains(root.left)
		if root.right is not None:
			return bt_contains(root.right)
	return False

def is_full(root):
	if root.left is None and root.right is None:
		return True
	else:
		if root.left is not None and root.right is not None:
			a = is_full(root.left)
			b = is_full(root.right)
			return a and b
	return False

def merge_bt(root1, root2):
	new = LinkedBinaryTree()
	new.root.data = root1.data + root2.data









def invert_bt(root):
	pass
def invert_bt(root):
	pass