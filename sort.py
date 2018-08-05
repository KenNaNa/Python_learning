'''
排序也是在程序中经常用到的算法。
无论使用冒泡排序还是快速排序，
排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，
但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来
'''

#Python内置的sorted()函数就可以对list进行排序
sor = sorted([12,3,4,5,613,345,234,566])
print(sor)

'''
sorted()函数也是一个高阶函数，
它还可以接收一个key函数来实现自定义的排序，
例如按绝对值大小排序
'''
print(sorted([36, 5, -12, 9, -21], key=abs))

'''
key指定的函数将作用于list的每一个元素上，
并根据key函数返回的结果进行排序。
对比原始的list和经过key=abs处理过的list
'''
'''
key指定的函数将作用于list的每一个元素上，
并根据key函数返回的结果进行排序。
对比原始的list和经过key=abs处理过的list：

list = [36, 5, -12, 9, -21]

keys = [36, 5,  12, 9,  21]
然后sorted()函数按照keys进行排序，
并按照对应关系返回list相应的元素：

keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
'''

strr = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(strr)
#即可实现忽略大小写的排序
strr = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(strr)
#要进行反向排序，
#不必改动key函数，
#可以传入第三个参数reverse=True
strr = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print(strr)


def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[-1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88),('at',20)]
L1 = sorted(L, key=by_name)
L2 = sorted(L, key=by_score)

print(L1)
print(L2)