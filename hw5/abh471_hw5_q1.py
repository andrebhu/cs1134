from ArrayStack import ArrayStack

def postfix(tokens):
	stack = ArrayStack()
	if len(tokens) == 1:
		return tokens[0]

	for token in tokens:
		if token.isdigit():
			stack.push(token)
		else:
			a = stack.pop()
			b = stack.pop()
			stack.push(str(eval(b + token + a)))
	return stack.top()

def main():
	assigned = {}
	while True:		
		tokens = input("--> ").split(" ")
		if tokens[0] == "done()":
			break
		else:
			for i in range(len(tokens)):
				if tokens[i] in assigned:
					tokens[i] = assigned[tokens[i]]

			if "=" in tokens:
				assigned[tokens[0]] = postfix(tokens[2:])
				print(tokens[0])
			else:
				print(postfix(tokens))

if __name__ == '__main__':
	main()