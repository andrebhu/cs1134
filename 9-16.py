def is_prime(num):
	for denom in range(2, num):
		if num % denom == 0:
			return False
	return True

def main():
	num = int(input("Test for prime on what number? "))
	print(is_prime(num))
main()