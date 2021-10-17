lst = [1, 2, 3]
lst_iter = iter(lst)
#print(lst_iter) #<list_iterator object at 0x01567148>
#print(next(lst_iter)) #1
#print(next(lst_iter)) #2
#print(next(lst_iter)) #3
try:
	print(next(lst_iter)) #StopIteration
except:
	pass

lst = [1, 2, 3]
lst_iter1 = iter(lst)
lst_iter2 = iter(lst)
#print(next(lst_iter1))
#print(next(lst_iter2))

#####################################################

s = "abc"
for item in s:
	print(item, end=" ")
print()

s = "abc"
s_iter = iter(s)
end = False
while(end == False):
	try:
		item = next(s_iter)
		#print(item, end=" ")
	except StopIteration:
		end = True
		
#####################################################
#Simulating the range(...) function

def my_range(start, stop, step):
	res = []
	curr = start
	while (curr < stop):
		res.append(curr)
		curr += step
	return res

for elem in my_range(3, 10, 0.5):
	print(elem, end=" ")

#####################################################
#Generators
print()
def f():
	x = 1
	yield x
	x  += 1
	yield x
	x += 1
	yield x

def my_range(start, stop, step):
	curr = start
	while curr < stop:
		yield curr
		curr += step

for elem in my_range(3, 10, 0.5):
	print(elem, end=" ")

#generators perform lazy evaluation
#produces an implicit iterable sequence
