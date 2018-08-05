'''
定义函数的时候，
我们把参数的名字和位置确定下来，
函数的接口定义就完成了。
对于函数的调用者来说，
只需要知道如何传递正确的参数，
以及函数将返回什么样的值就够了，
函数内部的复杂逻辑被封装起来，
调用者无需了解。

Python的函数定义非常简单，
但灵活度却非常大。除了正常定义的必选参数外，
还可以使用默认参数、可变参数和关键字参数，
使得函数定义出来的接口，不但能处理复杂的参数，
还可以简化调用者的代码
'''

def power2(x):
    return x*x
print(power2(10))

print(type('lijnwe'))
def len(str):
    if(type(str)=='(class "str")'):
        return len(str)
    else:
        return False
print(len('lijinwen'))


def powern(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powern(5,5))