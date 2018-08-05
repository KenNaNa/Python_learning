'''
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
在Python中，对匿名函数提供了有限支持。
还是以map()函数为例，计算f(x)=x2时，
除了定义一个f(x)的函数外，
还可以直接传入匿名函数
'''
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)
#lambda其实就是一个匿名函数
'''
跟javascript的匿名函数进行比较
var fs = function(i){
	return i
}
通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x
'''

f = lambda x:x * x
print(f)
print(f(2))
#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
print(build(1,2))
print(build(1,2)())