# -*- coding:utf-8 -*-

'''
from sys import argv

srcipt,user_name =argv
prompt = ">"
#prompt = "A："


print "Hi %s, i`m the %s srcipt." %(user_name,srcipt)
print "i`d like to ask you a few question."
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you like %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live in %r. not sure where that is. 
and you have a %r computer. nice.
""" % (lives,lives,computer)

'''

from sys import argv

srcipt,user_name,country =argv
prompt = ">"
#prompt = "A："


print "Hi %s, i`m the %s srcipt from %s." %(user_name,srcipt,country)
print "i`d like to ask you a few question."
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you like %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live in %r. not sure where that is. 
and you have a %r computer. nice.
""" % (lives,lives,computer)

