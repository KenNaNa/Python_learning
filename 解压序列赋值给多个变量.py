p = (4,5)
x,y = p
print(x)
print(y)
data = ['name','age','sex','address']
name,age,sex,address = data
print(name,age,sex,address)

data1 = ['name','age','sex','address',(2017,10,21)];
name,age,sex,address,date = data1
print(name,age,sex,address,date)
print(date)
#如果序列元素个数与变量个数不想等的话，会产生一个异常
'''
p = (4, 5)
>>> x, y, z = p
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack

'''
'''
实际上这种解压赋值可以是用在任何可以迭代对象上
而不仅仅是列表和元组
包括字符串 文件对象 迭代器 生成器
'''

s = 'hello'
a,b,c,d,e = s
print(a,b,c,d,e)#a=h,b=e,c=l,d=l,e=o
'''
有时候我并不需要解压所有的值 可能只需要一部分的值
对于Python没给出对应的方法
但是我们可以用变量去占位
到时候丢掉这些变量即可
'''