
'''

i = 0
numbers = []

while i < 6:
	print "at the top i is %d" %i
	numbers.append(i)

	i = i + 1
	print "numbers now:",numbers
	print "at the bottom i is %d \n" % i 

print "the numbers:"

for num in numbers:
	print num 

'''


numbers = []

def nub(i):
	for num in range(0,i):
		numbers.append(num)
	return numbers

#get_array = 
nub(6)

for num in numbers:
	print num 


















