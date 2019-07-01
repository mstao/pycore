# pycore [![Build Status](https://travis-ci.org/mstao/pycore.svg?branch=master)](https://travis-ci.org/mstao/pycore)

参考：

- 官方文档 https://docs.python.org/zh-cn/3/tutorial/
- Python教程 https://www.liaoxuefeng.com/wiki/1016959663602400

## 编码风格

- 使用4个空格缩进，不要使用制表符。
- 换行，使一行不超过79个字符。
- 使用空行分隔函数和类，以及函数内的较大的代码块。
- 如果可能，把注释放到单独的一行。
- 使用文档字符串。
- 在运算符前后和逗号后使用空格，但不能直接在括号内使用： `a = f(1, 2) + g(3, 4)`。
- 类和函数命名的一致性；规范是使用 `CamelCase` 命名类，`lower_case_with_underscores` 命名函数和方法。始终使用 self 作为第一个方法参数的名称（有关类和方法，请参阅 初探类 ）。
- 如果你的代码旨在用于国际环境，请不要使用花哨的编码。Python 默认的 UTF-8 或者纯 ASCII 在任何情况下都能有最好的表现。同样，哪怕只有很小的可能，遇到说不同语言的人阅读或维护代码，也不要在标识符中使用非ASCII字符。

参考：[PEP 8](https://www.python.org/dev/peps/pep-0008/PEP 8)

## 命名规范

Type |	Public | Internal
---|---|---
Modules	| lower_with_under	| 	_lower_with_under
Packages	| 	lower_with_under	 
Classes	| 	CapWords		| _CapWords
Exceptions	| 	CapWords	 
Functions	| 	lower_with_under()	| 	_lower_with_under()
Global/Class Constants		| CAPS_WITH_UNDER		| _CAPS_WITH_UNDER
Global/Class Variables	| 	lower_with_under	| 	_lower_with_under
Instance Variables	| 	lower_with_under	| 	_lower_with_under (protected) or __lower_with_under (private)
Method Names	| 	lower_with_under()		| _lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters	| 	lower_with_under	 
Local Variables	|	lower_with_under	
