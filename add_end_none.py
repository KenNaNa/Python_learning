def add_end_none(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

a = add_end_none()
print(a)

b = add_end_none()
print(b)
'''
为什么要设计str、None这样的不变对象呢？
因为不变对象一旦创建，对象内部的数据就不能修改，
这样就减少了由于修改数据导致的错误。
此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
同时读一点问题都没有。我们在编写程序时，
如果可以设计一个不变对象，
那就尽量设计成不变对象。


其实就跟js中的const 定义内容不可变的变量
'''