# -*- coding:utf-8 -*-

tabby_cat = "\ti`m tabbed in"
preson_cat = "i`m split\non a line"
backlash_cat = "i`m \\ a \\ cat"

fat_cat = """
i`ll do a list 
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""
fat_cat2 = '''
i`ll do a list 
\t* cat food
\t* fishies
\t* catnip\n\t* grass
'''

print tabby_cat
print preson_cat
print backlash_cat
print fat_cat
print fat_cat2

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

print 'I am 158cm\atall.'
print 'I am 158cm\ftall.'
print 'I am 158cm\ntall.'
print 'I am 158cm\vtall.'
print 'I am 158cm\ttall.'


a = "I am 6'2\" tall"
print "let`s talk about %s." % a
print "let`s talk about %r." % a

b = 'I am 6\'2" tall'
print "let`s talk about %s." % b
print "let`s talk about %r." % b


#a = "hhh" #"I am 6'2\" tall."
#print = " %r ", % a
#print = " %s ", % a

