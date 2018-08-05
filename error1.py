'''
错误处理
阅读: 177268
在程序运行的过程中，如果发生了错误，
可以事先约定返回一个错误代码，这样，
就可以知道是否有错，以及出错的原因。
在操作系统提供的调用中，返回错误码非常常见。
比如打开文件的函数open()，
成功时返回文件描述符（就是一个整数），出错时返回-1
'''

'''
用错误码来表示是否出错十分不便，
因为函数本身应该返回的正常结果和错误码混在一起，
造成调用者必须用大量的代码来判断是否出错
'''

def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass
# 一旦出错，还要一级一级上报，
# 直到某个函数可以处理该错误
# （比如，给用户输出一个错误信息）
# 所以高级语言通常都内置了一套
# try...except...finally...的错误处理机制，Python也不例外

try:
	print('正在尝试获取是否有错误')
	r = 10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('the error is :', e)
finally:
	print('结束了')
print('完成错误捕获')
'''
当我们认为某些代码可能会出错时，
就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，
而是直接跳转至错误处理代码，即except语句块，执行完except后，
如果有finally语句块，则执行finally语句块，至此，执行完毕
上面的代码在计算10 / 0时会产生一个除法运算错误：

try...
except: division by zero
finally...
END
由于没有错误发生，所以except语句块不会被执行，但是finally如果有，
则一定会被执行（可以没有finally语句）。

你还可以猜测，错误应该有很多种类，
如果发生了不同类型的错误，应该由不同的except语句块处理。
没错，可以有多个except来捕获不同类型的错误
'''
try:
	print('正在尝试获取是否有错误')
	r = 10/int('a')
	print('result:',r)
except ValueError as e:
	print('the error is :', e)
except ZeroDivisionError as e:
	print('the error is :', e)
else:
	# 如果没有报错
	print('no error')
finally:
	print('结束了')
print('完成错误捕获')

'''
Python的错误其实也是class，
所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，
它不但捕获该类型的错误，还把其子类也“一网打尽”
'''
try:
	foo()
except NameError as e:
	print('NameError')
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# 第二个except永远也捕获不到UnicodeError，
# 因为UnicodeError是ValueError的子类，
# 如果有，也被第一个except给捕获了
# 
# '''
# 使用try...except捕获错误还有一个巨大的好处
# 就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，
# 结果bar()出错了，这时，只要main()捕获到了，就可以处理
# '''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()

# 调用栈
# 如果错误没有被捕获，
# 它就会一直往上抛，
# 最后被Python解释器捕获，
# 打印一个错误信息，然后程序退出。来看看err.py
'''
记录错误
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，
但程序也被结束了。既然我们能捕获错误，
就可以把错误堆栈打印出来，然后分析错误原因，
同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息

'''
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')