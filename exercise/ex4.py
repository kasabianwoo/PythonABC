# -*- coding: utf-8 -*-


#定义变量cars
cars = 100
#定义变量space_in_car
space_in_car = 4.0
#定义变量drivers
drivers = 30
#定义变量passengers
passengers = 90
#定义变量cars_not_driven
cars_not_driven = cars - drivers
#定义变量cars_driven
cars_driven = drivers
#定义变量carpool_capacity
carpool_capacity = cars_driven * space_in_car
#定义变量average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

#打印变量cars
print "there are", cars, "cars available."
#打印变量drivers
print "there are only", drivers, "drivers available."
#打印变量cars_not_driven
print "there will be", cars_not_driven, "empty cars today."
#打印变量carpool_capacity
print "we can transport", carpool_capacity, "people today."
#打印变量passengers
print "we have", passengers, "to carpool today."
#打印变量average_passengers_per_car
print "we need to put about", average_passengers_per_car,"in each car"


#字符串拼接
#print "Hey %s there." % "you"
