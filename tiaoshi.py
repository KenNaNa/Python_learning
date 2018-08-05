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
'''
用print()最大的坏处是将来还得删掉它，
想想程序里到处都是print()，
运行结果也会包含很多垃圾信息。
所以，我们又有第二种方法
'''

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()
'''
assert的意思是，表达式n != 0应该是True，
否则，根据程序运行的逻辑，后面的代码肯定会出错
如果断言失败，assert语句本身就会抛出AssertionError
把print()替换为logging是第3种方式，和assert比，
ogging不会抛出错误，而且可以输出到文件
'''
print('-----------------------')
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)