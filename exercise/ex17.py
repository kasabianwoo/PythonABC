# -*- coding:utf-8 -*-

'''
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "copying from %s t0 %s" %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "does the output file exists? %r" % exists(to_file)
print "ready,hit return to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()

'''

from sys import argv
from os.path import exists

script,from_file,to_file = argv

in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

