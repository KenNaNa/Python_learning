'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，
其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce
def add(x,y):
	return x+y
var = reduce(add,[1,2,3,4,5,6,7,8])
print(var)
print(sum([1,2,3,4,5,6,7,8]))
#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce
#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，
#reduce就可以派上用场
#
#这个例子本身没多大用处，但是，
#如果考虑到字符串str也是一个序列，
#对上面的例子稍加改动，配合map()，
#我们就可以写出把str转换为int的函数
def fn(x,y):
	return x*10+y
def char2num(s):
	d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return d[s]
num = reduce(fn,map(char2num,'1009'))
print(num)