def add_end(L=[]):
	L.append('END')
	return L

a = add_end([1,2,3])
print(a)
b = add_end([1,2,3,'end'])
print(b)
'''
Python函数在定义的时候，
默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，
如果改变了L的内容，则下次调用时，
默认参数的内容就变了，不再是函数定义时的[]了。
'''
#定义默认参数要牢记一点：默认参数必须指向不变对象！
c = add_end()
d = add_end()
print(c)
