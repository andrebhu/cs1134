from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
	if bst.root is None:
		raise Exception("tree is empty")
		
	lst = [item for item in bst]
	if len(lst) == 1:
		return lst[0]
	else:
		m = lst[1] - lst[0]
		for i in range(2, len(lst) - 1):
			m = min(m, lst[i] - lst[i - 1])
		return m