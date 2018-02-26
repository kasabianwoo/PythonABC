

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

