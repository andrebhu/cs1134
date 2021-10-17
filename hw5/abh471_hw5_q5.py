from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
	stack = ArrayStack()
	queue = ArrayQueue()

	for i in lst:
		stack.push(i)

	queue.enqueue([stack.pop()])

	while stack.is_empty() == False:
		new = stack.pop()
		for i in range(len(queue)):
			for pos in range(len(queue.first()) + 1):
				e = queue.first().copy()
				e.insert(pos, new)
				queue.enqueue(e)
			queue.dequeue()

	r = []
	while queue.is_empty() == False:
		r.append(queue.dequeue())
	return r

#print(permutations([1, 2, 3]))