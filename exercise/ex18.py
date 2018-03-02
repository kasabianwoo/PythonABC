# -*- coding:utf-8 -*-

def print_two(*args):
	arg1,arg2 = args
	print "arg1:%r,arg2:%r" %(arg1,arg2)

def print_two_again(arg3,arg4):
	print "arg3:%r,arg4:%r" %(arg3,arg4)

def print_one(arg5):
	print "arg5:%r" % arg5

def print_none():
	print "i got nothin'."

print_two("kasabian","woo")
print_two_again("zed","shaw")
print_one("frist!")
print_none()

