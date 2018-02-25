# -*- coding: utf-8 -*-

my_name = 'kasabian woo'
my_age = 33
my_height = 158 #cm
my_weight = 58 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "let`s talk about %s." % my_name
print "he`s %d cm tall." % my_height
print "he`s %d kg heavy." % my_weight
print "actually that`s not too heavy."
print "he`s got %s eyes and %s hair." % (my_eyes, my_hair)
print "his teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "if i add %d, %d, and %d i get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
#print ""