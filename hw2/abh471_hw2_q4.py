def e_approx(n):
	r = 1.0
	denom = 1.0
	for i in range(1, n + 1):
		denom *= i
		r += (1 / denom)
	return r

'''
def main():
	for n in range(15):
		curr_approx = e_approx(n)
		approx_str = "{:.15f}".format(curr_approx)
		print("n =", n, "Approximation:", approx_str)
main()
'''
