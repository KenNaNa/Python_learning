'''
sl       console  Nov 21 08:59 
sl       ttys000  Nov 21 09:09 
sl       ttys001  Nov 21 10:30 
'''
import re


f = open('whodata.txt','r')
for eachLine in f:
    print(re.split(r'\s\s+', eachLine))
f.close()
'''
['sl', 'console', 'Nov 21 08:59', '']
['sl', 'ttys000', 'Nov 21 09:09', '']
['sl', 'ttys001', 'Nov 21 10:30 ']
'''
'''
上面的程序，who命令是在脚本外部执行的，
每次手动重复做这件事让人很厌倦，
我们可以通过调用os.popen()命令（
现在已经被subprocess模块替代）将这个命令的执行在脚本内部实现。
另外我们使用str.rstrip()去除尾部的\n
'''

f = open('whodata.txt','r')
for eachLine in f:
    print(re.split(r'\s\s+', eachLine.rstrip()))
f.close()
'''
['sl', 'console', 'Nov 21 08:59']
['sl', 'ttys000', 'Nov 21 09:09']
['sl', 'ttys001', 'Nov 21 10:30']
'''

'''
还可以使用with语句，可以使上下文管理对象变得更简易
'''
# import os

# f = os.popen('who', 'r')
# for eachLine in f:
#     print(re.split(r'\s\s+|\t', eachLine.rstrip()))
# f.close()
print('-------------------------')
with open('whodata.txt','r') as f:
	for eachLine in f:
		print(re.split(r'\s\s+', eachLine.rstrip()))
'''
['sl', 'console', 'Nov 21 08:59']
['sl', 'ttys000', 'Nov 21 09:09']
['sl', 'ttys001', 'Nov 21 10:30']
'''

'''
如果要适配python2和python3的话，
可以避免使用print（）,
而使用两个版本中都有的函数distutils.log.warn()，
并将其转换成printf名来使用
'''
from distutils.log import warn as printf
with open('whodata.txt', 'r') as f:
    for eachLine in f:
        printf(re.split(r'\s\s+|\t', eachLine.rstrip()))
print('----------------------------')
# 生成随机数的例子，用于希望练习从中匹配、搜索正则表达式使用：
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edo', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize) / 3000000000
    dtstr = ctime(dtint)n))
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(lle
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
'''
Sun Dec 20 00:10:35 2037::ftmlsda@alccmfovz.gov::2144851835-7-9
Wed Oct 22 06:40:35 2053::cqqqgti@vpzvadyk.gov::2644699235-7-8
Mon Oct 11 02:51:31 1999::mkokoq@aifmmjs.net::939581491-6-7
Mon Jul  1 15:01:13 2019::plhg@cpvjdttv.edo::1561964473-4-8
Tue Jan 20 21:02:40 2004::wtsuq@tgchqciwu.edo::1074603760-5-9
Wed Jul 16 09:02:11 2036::ebmj@ufarwiszfkhq.net::2099782931-4-12
Tue Dec 29 19:52:43 2065::idhw@jvgxdfzi.edo::3029313163-4-8
Thu Sep 17 04:05:37 2020::uwkmur@nnqlhpy.org::1600286737-6-7
Fri Mar 24 01:28:54 2028::vjzky@qjmagcxp.net::1837445334-5-8
'''