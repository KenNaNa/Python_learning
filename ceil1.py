# 动态语言和静态语言最大的不同，就是函数和类的定义，
# 不是编译时定义的，而是运行时动态创建的
# 
class Hello(object):
	def hello(self,name = 'world'):
		print('Hello,%s' % name)

h = Hello()
h.hello()