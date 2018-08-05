'''
如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，
你就能大概明白map/reduce的概念。
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回
'''
def f(x):
	return x * x
arrList = [1,2,3,4,5,6]
I = map(f,arrList)
print(I)
L = list(I)
print(L)
'''
map()传入的第一个参数是f，即函数对象本身。
由于结果r是一个Iterator，Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list
'''
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
'''
map()作为高阶函数，事实上它把运算规则抽象了，因此，
我们不但可以计算简单的f(x)=x2，
还可以计算任意复杂的函数
'''
Li = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(Li)
# tuplel = list(map([1,2,3]))
# print(tuplel)
# 会报错