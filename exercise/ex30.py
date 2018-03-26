# -*- coding:utf-8 -*-


'''
#定义参数
people = 30
cars = 30
trucks = 40


#如果cars > people，那么... 如果cars < people，那么... 其他情况就...

if cars > people:
	print "we should take the cars."
elif cars < people:
	print "we should not take the cars."
else:
	print "we cant't decide."

#如果trucks > cars，那么... 如果trucks < cars，那么... 其他情况就...

if trucks > cars:
	print "that's too many trucks"
elif trucks < cars:
	print "maybe we could take the trucks."
else:
	print "we still can't decide"	

#如果people > trucks，那么... 其他情况就...

if people > trucks:
	print "allright,let's just take the trucks"
else:
	print "fine,let's stay home then"


'''

people = 30
cars = 30
trucks = 40

if trucks > cars and trucks + cars <= people :
	print "maybe we could take the trucks."
else:
	print "fine,let's stay home then"

