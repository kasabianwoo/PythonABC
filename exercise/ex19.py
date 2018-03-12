# -*- coding:utf-8 -*-

def cheese_and_crackers(cheese_count,boxex_of_crackers): #定义函数
	print "you have %s cheese!" % cheese_count
	print "you have %s boxes of crackers!" % boxex_of_crackers
	print "man that's enough for a party"
	print "get a blanket.\n"

'''
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)  #定义函数变量cheese_and_crackers，直接以数字方式

print "or,we can use variable from our script:"
amout_of_cheese = 10  #定义变量amout_of_cheese
amout_of_crackers = 50 #定义变量amout_of_crackers

cheese_and_crackers(amout_of_cheese,amout_of_crackers)  #重新定义函数变量cheese_and_crackers，已调用脚本变量的方式

print "we can even do math inside too:"
cheese_and_crackers(10+20,5+6) #重新定义函数变量cheese_and_crackers，以数字计算的方式

print "and we can combine the two, variable and math:"
cheese_and_crackers(amout_of_cheese+100,amout_of_crackers+1000) #重新定义函数变量cheese_and_crackers，变量+数字

'''


#10种方法运行这个函数


print "5th method:"   // 需要更改line4和line5中的%d为%s
amout_of_cheese = raw_input("amout_of_cheese>")
amout_of_crackers = raw_input("amout_of_crackers>")
cheese_and_crackers(amout_of_cheese,amout_of_crackers)

print "6th method:" // 需要更改line4和line5中的%d为%s
print "amout_of_cheese>"
amout_of_cheese = raw_input()
print "amout_of_crackers>"
amout_of_crackers = raw_input()
cheese_and_crackers(amout_of_cheese,amout_of_crackers)

print "7th method:" 
amout_of_crackers = raw_input("amout_of_crackers>")
cheese_and_crackers(20,amout_of_crackers)

print "8th method:" 
amout_of_cheese = 20
amout_of_crackers = raw_input("amout_of_crackers>")
cheese_and_crackers(amout_of_cheese,amout_of_crackers)

print "9th method:" 
amout_of_crackers = raw_input("amout_of_crackers>")
cheese_and_crackers(20+100,amout_of_crackers)

print "10th method:" 
amout_of_cheese = 20
amout_of_crackers = raw_input("amout_of_crackers>")
cheese_and_crackers(amout_of_cheese+100,int(amout_of_crackers)+1000)



