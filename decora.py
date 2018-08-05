'''
由于函数也是一个对象，
而且函数对象可以被赋值给变量，
所以，通过变量也能调用该函数
'''
def now():
	print('2015-3-25')
now()
#函数对象有一个__name__属性，可以拿到函数的名字
#跟javascript的 es6的属性name太像了
print(now.__name__)

'''
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，
称之为“装饰器”（Decorator）
'''
#本质上，decorator就是一个返回函数的高阶函数。
#所以，我们要定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()
'''
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)
'''

#说的通俗易懂的话就是函数嵌套嘛，
#什么鬼的修饰器
#搞的怎么难懂
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')

#now = log('execute')(now)
print(now.__name__)#wrapper
'''
因为返回的那个wrapper()函数名字就是'wrapper'，
所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错
'''