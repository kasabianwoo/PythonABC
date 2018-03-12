# -*- coding:utf-8 -*-

'''
from sys import argv 

script,input_file = argv   #定义 argv，调用输入

def print_all(f):
    print f.read()         #定义函数 print_all，读取整个文件

def rewind(f):
    f.seek(0)              #定义函数 rewind，让”磁头“位置回到文件开头

def print_a_line(line_count,f):
	print line_count,f.readline()     #定义函数 print_a_line, 打印行数和读取文件1行

current_file = open(input_file)       #设置变量为打开文件

print "First let's print the whole file:\n"
print_all(current_file)                         #使用一次函数print_all

print "Now let's rewind, kind of like a tape."
rewind(current_file)                            #使用一次函数rewind     

current_line = 1                                #连续用3次函数print_a_line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

'''

def nub(n):
	print "i get the number: %s" % n

count = 5
nub(count)

count += 5
nub(count)

count += 5
nub(count)

