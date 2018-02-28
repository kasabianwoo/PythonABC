

01、编码错误

```
File "[ex1.py](http://ex1.py)", line 6

SyntaxError: Non-ASCII character '\xe2' in file [ex1.py](http://ex1.py) on line 6, but no encoding declared; see [http://python.org/dev/peps/pep-0263/](http://python.org/dev/peps/pep-0263/) for details
```

在第一行添加 `# -*- coding: utf-8 -*-` 解决。



03、错用等式和判断式

```
File "[ex3.py](http://ex3.py)", line 21

   print "is it greater or equal?",5≥-2

                                    ^

SyntaxError: invalid syntax
```

把“≥/≤”等同于“>=/<=”了，“>=/<=”是判断式，“≥/≤”是等式。



07、false 第一个字母要大写

```
Traceback (most recent call last):
  File "ex6.py", line 14, in <module>
    hilarious = false 
NameError: name 'false' is not defined
```

False才对



08、中文状态下输入引号导致的错误

```
$ python ex7.py
File "ex7.py", line 4
    print "its fleece was white as %s." % ‘snow’
                                          ^
SyntaxError: invalid syntax
```

```
$ python ex7.py
mary had a little lamb
Traceback (most recent call last):
  File "ex7.py", line 4, in <module>
    print "its fleece was white as %s." % snow
NameError: name 'snow' is not defined
```



09、



```
  File "ex8.py", line 2
    formatter = “%r %r %r %r”
                ^
SyntaxError: invalid syntax
```

修改为英文下的引号。


```
Traceback (most recent call last):
  File "ex8.py", line 5, in <module>
    print formatter % (one,two,three,four)
NameError: name 'one' is not defined
```

修改： one、two、three four 加引号。格式化字符串引用文本时需带上引号（单引号和双引号均可）。



```
File "ex8.py", line 6, in <module>
    print formatter % (ture,fause,ture,fause)
NameError: name 'ture' is not defined
```

修改 ture 为 true ，修改 fause 为 false



```
1 2 3 4
'one' 'two' 'three' 'four'
True False True False
Traceback (most recent call last):
  File "ex8.py", line 8, in <module>
    "i had this thing."
TypeError: not enough arguments for format string
```

字符串的参数不足，9-11行添加“，”号，这里为4个字符串；


```
$ python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False True False
'i had this thing.' 'that you could type up right.' 'but it didn\xe2\x80\x98t sing.' 'so i said goodnight.'
```

\xe2\x80\x98, 使用单引号，而非“`”。 英文“don't”的省略形式中的符号为单引号！









17、

```
$ python ex16.py test.txt
we`re going to erase 'test.txt'.
if you don`t want that,hit CTRL-C (^C)
if you do want that, hit RETURMN
?
opening the file...
truncating the file. goodbye!
now i`m going to ask you for three lines.
line1:1
line2:2
line3:3
i`m going to write these to the file.
Traceback (most recent call last):
  File "ex16.py", line 31, in <module>
    target.write(lin3)
NameError: name 'lin3' is not defined
```

书写错误，lin3应该为 line3。（ 我检查了代码么？）


```
$ python ex16.py test.txt
we`re going to erase 'test.txt'.
if you don`t want that,hit CTRL-C (^C)
if you do want that, hit RETURMN
?
opening the file...
truncating the file. goodbye!
now i`m going to ask you for three lines.
line1:1
line2:2
line3:3
i`m going to write these to the file.
Traceback (most recent call last):
  File "ex16.py", line 34, in <module>
    print target.readline()
IOError: File not open for reading
```

可能原因是文件已经在写入状态了`target = open(filename, 'w')`, 把其他代码注释掉，仅保留 readline() 代码，返回了文件的第一行内容：