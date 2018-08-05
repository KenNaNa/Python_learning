from collections import Iterable
def add(a,b):
	print(a,b)
print(isinstance('str',Iterable))
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance(123,Iterable))
print(isinstance(add,Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance((),Iterable))

#可以使用isinstance()判断一个对象是否是Iterator对象
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
from collections import Iterator
print(isinstance('str',Iterator))#false
print(isinstance(iter('str'),Iterator))#true
# print(isinstance(iter(123),Iterator))
'''
这是因为Python的Iterator对象表示的是一个数据流，
Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，
但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，
所以Iterator的计算是惰性的，
只有在需要返回下一个数据时它才会计算。
'''