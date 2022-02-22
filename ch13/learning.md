# 第13章 文件的读写

## 13.7 使用struct模块读取结构化二进制数据

使用`struct`模块读写二进制字节

```python
>>> import struct
>>> struct_format = 'hd4s'
>>> struct.pack(struct_format, 4, 3.21, b'aDay')
b'\x04\x00\x00\x00\x00\x00\x00\x00\xaeG\xe1z\x14\xae\t@aDay'
```

## 13.8 使用pickle模块存放对象到文件中

```python
>>> import pickle
>>> file = open('state', 'wb')
>>> a = 3.14
>>> b = 'hello world'
>>> c = [1, 2, 3]
>>> pickle.dump(a, file)
>>> pickle.dump(b, file)
>>> pickle.dump(c, file)
>>> file.close()
>>> 
>>> file = open('state', 'rb')
>>> a = pickle.load(file)
>>> a
3.14
>>> b = pickle.load(file)
>>> b
'hello world'
>>> c = pickle.load(file)
>>> c
[1, 2, 3]
>>> file.close()
```

## 13.9 使用shelve保存对象

```python
>>> import shelve
>>> file = shelve.open('addresses')
>>> file['Nightwing'] = ('Dick', 'Grasson')
>>> file['Batman'] = ('Bruce', 'Wyen')
>>> file['Redhood'] = ('Jesson', 'Tord')
>>> file.close()
>>> book = shelve.open('addresses')
>>> book['Nightwing']
('Dick', 'Grasson')
>>> book['Redhood']
('Jesson', 'Tord')
```
