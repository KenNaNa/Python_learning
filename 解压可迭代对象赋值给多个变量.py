# -*- coding: utf-8 -*-
#这个时候*表达式就突出其作用了
#定义一个函数
def drop_first_last(grades):
    first,*middle,last = grades
    return avg(middle)
def avg(middle):
    sum = 0
    for val in middle:
        sum += val
    return sum
print(drop_first_last([12,3,45,66,77,888,100]))
'''
Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期
末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如
果只有四个分数，你可能就直接去简单的手动赋值，但如果有 24 个呢？这时候星号表
达式就派上用场了：

'''
'''
如果一个可以迭代对象的元素的个数超过变量的个数 会抛出一个异常
那么我们该如何从这个异常里获取出N个元素呢
'''

'''
另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮
件，接着就是不确定数量的电话号码。你可以像下面这样分解这些记录：
'''

record = ('Devid','devid@eaxmple.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record
print(name,email)
print(phone_numbers)#['773-555-1212', '847-555-1212']
'''
值得注意的是phone_numbers解压后总是一个列表 所以我们就不用每次
都多余的去判断phone_numbers是否是一个列表
'''

'''
星号表达式也能用在列表的开始部分。比如，你有一个公司前 8 个月销售数据的序
列，但是你想看下最近一个月数据和前面 7 个月的平均值的对比。你可以这样做：
'''
sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
def sum(trailing_qtrs):
    sums = 0
    for val in trailing_qtrs:
        sums += val
    return sums
def avg_comparison(trailing_avg,current_qtr):
    if trailing_avg>current_qtr:
        return True
    else:
        return False
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(avg_comparison(trailing_avg, current_qtr))#True
print(trailing_qtrs)#[10, 8, 7, 1, 9, 5, 10]
print(current_qtr)#3

'''
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计
的。通常，这些可迭代对象的元素结构有确定的规则（比如第 1 个元素后面都是电话
号码），星号表达式让开发人员可以很容易的利用这些规则来解压出元素来。而不是通
过一些比较复杂的手段去获取这些关联的的元素值。
'''
'''
值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。比如，
下面是一个带有标签的元组序列：
'''
maxium = max(1,2,3)
minium = min(23,12,34)
print(maxium,minium)#3,12


records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)
for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)
'''
星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
'''
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)#nobody
print(fields)#['*', '-2', '-2', 'Unprivileged User']
print(homedir)#/var/empty
print(sh)#/usr/bin/false
for val in fields:
    print(val)


'''
有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一
个普通的废弃名称，比如 或者 ign 。
'''

record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year) = record
print(name)
print(year)
print(*_)#12,18

'''
在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有
一个列表，你可以很容易的将它分割成前后两部分：
'''
items = [1, 10, 7, 4, 5, 9]
item,*args = items;
print(item,args)#1 [10, 7, 4, 5, 9]
