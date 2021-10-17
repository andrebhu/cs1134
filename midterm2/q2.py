def owe(months, dollars):
	if months == 0:
		return 0
	else:
		return dollars + owe(months - 1, dollars * 1.015)
'''
print(owe(0, 100))
print(owe(1, 25))
print(owe(2, 100))
print(owe(3, 100))
'''