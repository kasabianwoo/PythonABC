# -*- coding:utf-8 -*-

'''
def add(a,b):
    return a + b

return_test = add(10,20) 

print "%d" % return_test

'''

def add(a,b):
	print "adding %d + %d" %(a,b)
	return a+b

def subtract(a,b):
	print "subtracting %d - %d" %(a,b)
	return a-b

def multiply(a,b):
	print "multiplying %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "dividing %d / %d" %(a,b)
	return a/b

print "let's do something math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "age:%d,height:%d,weight:%d,iq:%d" %(age,height,weight,iq)

print "here is a puzzle."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

'''
divide(iq,2)
multiply(weight,divide(iq,2))
subtract(height,multiply(weight,divide(iq,2)))
'''

print "that becomes:",what,"can you do it by hand?"


