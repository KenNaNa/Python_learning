print(type(123))#跟javascript的typeof 非常像

'''
<class 'int'>
<class 'str'>
<class 'type'>
<class 'NoneType'>
'''

print(type('123'))

class Animal(object):
	pass
print(type(Animal))

print(type(None))


'''
True
False
True
True
True
False
'''
print(type(123)==type(456))

print(type('1233')==type(1233))

print(type(123)==int)

print(type('122')==type('1223'))

print(type('123')==str)

print(type('abc')==type(122))

'''
但如果要判断一个对象是否是函数怎么办？
可以使用types模块中定义的常量
'''

import types
def fn():
	print('fn')

print(type(fn)==types.FunctionType)

print(type(fn)==types.BuiltinFunctionType)

print(type(lambda x:x)==types.LambdaType)

print(type((x for x in range(10)))==types.GeneratorType)

'''
True
False
True
True
'''

'''
对于class的继承关系来说，
使用type()就很不方便。
我们要判断class的类型，
可以使用isinstance()函数
跟javascript实在是太像了
'''
print('-------------------------------------')
import duotaijic

a = list()
b = Animal()
# c = Dog()
# d = Sheep()

print(isinstance(b,Animal))
# print(isinstance(c,Dog))
# print(isinstance(d,Sheep))

# print(isinstance(c,Animal))
# print(isinstance(d,Animal))
# 
# 能用type()判断的基本类型也可以用isinstance()判断
# 
print('***********************************')

print(isinstance('123',str))
print(isinstance(123,int))
print(isinstance(b'z',bytes))

#并且还可以判断一个变量是否是某些类型中的一种，
#比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1, 2, 3], (list, tuple)))

print(isinstance((1, 2, 3), (list, tuple)))

#使用dir()
'''
如果要获得一个对象的所有属性和方法，
可以使用dir()函数，它返回一个包含字符串的list，
比如，获得一个str对象的所有属性和方法
'''

print(dir(abs))
print('---------------------------------------------------------')
print(dir('abc'))

print('abc'.__len__())
print(len('abc'))

print('a-b-c'.split('-'))

#我们自己写的类，如果也想用len(myObj)的话，
#就自己写一个__len__()方法

class Mydog(object):
	def __len__(self):
		return 100

dog = Mydog()
print(dog.__len__())

print('ABC'.lower())
a = 'ABC'.join('-');
print(a)

print('ABC'.startswith('A'))

print('ABC'.translate('a'))#'ABC'

print('ABC '.strip())#'ABC'

print('ABC'.isupper())#true
print('ABC'.islower())#false

'''
仅仅把属性和方法列出来是不够的，
配合getattr()、setattr()以及hasattr()，
我们可以直接操作一个对象的状态
'''

class Myobject(object):
	def __init__(self):
		self.x = 9
	def getName(self):
		return self.x
	def power(self):
		return self.x * self.x


obj = Myobject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))

print(hasattr(obj,'power'))

print(setattr(obj,'y',29))

print(getattr(obj,'y'))

print(getattr(obj,'power'))

print(id(obj))

print(id(obj.power()))


'''
假设我们希望从文件流fp中读取图像，
我们首先要判断该fp对象是否存在read方法，
如果存在，则该对象是一个流，如果不存在，
则无法读取。hasattr()就派上了用场
'''
def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None