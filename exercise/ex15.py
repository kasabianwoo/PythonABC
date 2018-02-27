# -*- coding:utf-8 -*-


'''
#argv 格式，从 sys 调用
from sys import argv

#argv 的2个参数
script,filename = argv

#以变量的方式打开文件filename
txt = open(filename)

#打印
print "here`s your file %r:" % filename
#打印...读出变量 a 对应的文件
print txt.read()

#打印
print "type the filename again:"
#以变量的方式调用输入
file_again = raw_input(">")

#以变量的方式，打开变量 file_again对应的文件
txt_again = open(file_again)

#打印...读取变量txt_again对应的文件
print txt_again.read()

txt.close()
txt_again.close()
'''



filename = raw_input("filename:")

txt = open(filename)

print "here`s your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)

print txt_again.read()


