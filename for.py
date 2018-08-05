# -*- coding: utf-8 -*-
# 
import os
L = []
n = 1
while n<=99:
    L.append(n)
    n = n + 2

print(L)

arr = list(range(1,11))
print(arr)

L = []
for x in list(range(1,11)):
	L.append(x*x)
print(L)


a = []
for x in range(1,11):
	a.append(x*x)
print(a)

b = [x * x for x in range(1, 11)]
print(b)

c = [m+n for m in 'ABC' for n in 'XYZ']
print(c)

L = []
for m in 'ABC':
	for n in 'XYZ':
		L.append(m+n)

print(L)

print(os)
arr = [d for d in os.listdir('.')] 
print(arr)#运用列表生成式，
#可以写出非常简洁的代码。
#例如，列出当前目录下的所有文件和目录名
#
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'==',v)

e = [k+'=='+v for k,v in d.items()]
print(e)

L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
print(l)


L1 = ['Hello', 'World', 18, 'Apple', None]

l2 = [x.lower() for x in L1 if isinstance(x,str) ]
print(l2)


L = ['Hello', 'World', 18, 'Apple', None]
L2=[str.lower(i) for i in L if isinstance(i,str)]
print(L2)

L2 = [i.lower() for i in L1 if isinstance(i,str)==1]
print(L2)


print('-------')
for i in range(0,10):
	print(i)