# The Quick Python Book (Third Edition) Python快速入门(第三版) 笔记

内置函数:

```Python
len()
sorted()
```

## 第5章 列表、元组和集合

列表相关函数：
x = [1, 2, 3, 4]
|列表x的方法|x|说明|
|-|-|-|
|`x.append("five")`|[1, 2, 3, 4, 'five']|在列表最后添加一个新元素|
|`x.extend([5, 6])`|[1, 2, 3, 4, 5, 6]|在列表后面添加新元素，如果待添加的是一个列表，则该列表会连接到原列表后面组成新列表|
|`x.insert(0, "first")`|['first', 1, 2, 3, 4]||
|`x.remove(4)`|[1, 2, 3]|从头开始查找第一个给定值的实例并且删除|
|`x.reverse()`|[4, 3, 2, 1]|反转列表|

### 5.2 列表的索引机制

1. 切片的使用：`list[index1:index2]`,返回`list`列表索引从`index1`(包含)到`index2`(不包含)前一位.除非`index2`没有指定，则返回到最后一位

```Python
>>> x = [1, 2, 3, 4]
    y = [0: 3]
    z = [:]
>>> y
[1, 2, 3]
>>> z
[1, 2, 3, 4]
```

2. 在python列表中使用切片，会返回一个新(创建)的列表,此时对两列表的操作互不影响

```Python
>>> x = [1, 2, 3, 4]
    y = x[:]
    y[0] = 5
>>> x
[1, 2, 3, 4]
>>> y
[5, 2, 3, 4]
```

---

## 第6章 字符串

### 6.6.3 格式描述符

默认情况下，格式字符串中参数如果是数字，则默认右对齐；如果是字母，则默认左对齐

```python
>>> x = "{a:{b}}".format(a = 1, b = 5)
>>> x
'    1' #默认右对齐
>>> x = "{a:<{b}}".format(a = 1, b = 5)
>>> x
'1    ' #设置为左对齐
>>> x = "{a:{b}}".format(a = "a", b = 5)
>>> x
'a    ' #默认左对齐
```

### 6.7.1 使用格式化序列

使用字符串取模操作符%,默认对数字进行右对齐

```python
>>> "Pis is <%-6.2f>" % 3.1415926
'Pis is <3.14  >' #添加-强制左对齐
>>> "Pis is <%6.2f>" % 3.1415926
'Pis is <  3.14>' #默认右对齐
```

---
## 第8章 流程控制

### 8.5 语句、代码块和缩进
`\`可以用来对字符串进行换行输入，如果`\`出现在引号内，则`\`之后的所有空白符都会被解释;如果出现在引号外，则只拼接引号内的字符串

```python
>>> x = 1
>>> x
1
>>> if x > 0: 
	string1 = "this string broken by a backslash will end up \
		with the indentation tabs in it" # 出现在引号内

	
>>> string1
'this string broken by a backslash will end up \t\twith the indentation tabs in it'
>>> if x > 0:
	string1 = "this string broken by a backslash will end up" \
		"with the indentation tabs in it" #出现在引号外

	
>>> string1
'this string broken by a backslash will end upwith the indentation tabs in it'
```