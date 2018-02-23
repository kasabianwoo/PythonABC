

01、编码错误

```
File "[ex1.py](http://ex1.py)", line 6

SyntaxError: Non-ASCII character '\xe2' in file [ex1.py](http://ex1.py) on line 6, but no encoding declared; see [http://python.org/dev/peps/pep-0263/](http://python.org/dev/peps/pep-0263/) for details
```

在第一行添加 `# -*- coding: utf-8 -*-` 解决。



02、错用等式和判断式

```
File "[ex3.py](http://ex3.py)", line 21

   print "is it greater or equal?",5≥-2

                                    ^

SyntaxError: invalid syntax
```

把“≥/≤”等同于“>=/<=”了，“>=/<=”是判断式，“≥/≤”是等式。