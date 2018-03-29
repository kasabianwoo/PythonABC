

the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
changes = [1,'pennies',2,'dimes',3,'quarters']

for haha in the_count:
    print "This is count %d" % haha

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in changes:
	print "i got %r" % i


elements = range (6)

#for i in range(6):
 #   print "Adding %d to the list." % i
 #   elements.append(i)

#elements.append(the_count)

elements.append(6)

for i in elements:
	print i 