import re
regx = r'^mina'
s = 'mina'
# 1.测试正则表达式是否匹配整个字符串
print(re.match(regx,s))
print(re.match(regx,s).group())

# 2.测试正则表达式是否匹配字符串的全部或部分
print(re.search(regx,s))
print(re.search(regx,s).group())

# 3.创建一个匹配对象
m = re.search(regx,s)
if m:
	print('您匹配成功了')
else:
	print('您匹配失败了')

# 4.获取正则表达式所匹配的子串
if m:
	g = m.group()
	print(g)
else:
	print(m)

# 6. 获取有名组所匹配的子串
d = r'^(\d{3})-(\d{3,8})$'
s = '010-12345678'
m = re.match(d,s)
if m:
	g1 = m.group(0)
	print(g1)
	g2 = m.groups()
	print(g2)
else:
	print(m)

# 7. 将字符串中所有匹配的子串放入数组中
result = re.findall(d,s)
print(result)#[('010', '12345678')]
print(type(result))

# 8.遍历所有匹配的子串
for v in result:
	print(v)

# 9.通过正则表达式字符串创建一个正则表达式对象
m = re.compile(d)

print(m)
print(m.search(s))
print(m.search(s).group(0))
print(m.search(s).group(1))
print(m.search(s).group(2))
print(m.search(s).groups())


print('---------------------------------------')
reg = r'[^\d]+'
s = '010-12345678'
print(re.match(reg,s))#None
print(re.search(reg,s))#<_sre.SRE_Match object; span=(3, 4), match='-'>
print(re.findall(reg,s))#['-']
s = 'qbc-'
print(re.findall(reg,s))
print(re.search(reg,s))
print(re.match(reg,s))

# 4.匹配单词边界：“\b”、“\B”
# \b：匹配单词的边界（单词前或后），而不在乎单词中间的字符
# \B：匹配单词中间的字符，而不在乎单词边界的字符
reg = r'er\B'
s = 'verb'
print(re.match(reg,s))#None
print(re.search(reg,s))#<_sre.SRE_Match object; span=(1, 3), match='er'>
print(re.findall(reg,s))
reg = r'er\b'
s = 'ber'
print(re.match(reg,s))#None
print(re.search(reg,s))#<_sre.SRE_Match object; span=(1, 3), match='er'>
print(re.findall(reg,s))

# match() :从字符串开始的位置匹配，成功返回匹配的对象，失败返回None
# search(): 扫描整个字符串来进行匹配，成功返回匹配的对象，失败返回None
import re
print('---------------------')
m = re.match('foo', 'seafood')
if m is not None: 
	print("match-" + m.group())

m = re.search('foo', 'seafood')
if m is not None: 
	print("search-" + m.group())

print('---------------------------')
# 例2: match()函数从起始位开始匹配
m = re.match('foo', 'foo')
if m is not None:
    print("能匹配-" + m.group())

m = re.match('foo', 'bar')
if m is not None: print("不能匹配-" + m.group())

m = re.match('foo', 'food on the table')
if m is not None: print("从开始位置进行匹配-" + m.group())

#能匹配-foo
#从开始位置进行匹配-foo
#
#例3: 匹配多个值（使用择一表达式"|"）
print('-------------------')
bt = 'bat|bet|bit'

m = re.match(bt, 'bat')
if m is not None:
    print("1能匹配-" + m.group())


m = re.match(bt, 'blt')
if m is not None:
    print("2能匹配-" + m.group())


m = re.match(bt, 'he bit me')
if m is not None:
    print("3能匹配-" + m.group())


m = re.search(bt, 'he bit me')
if m is not None:
    print("4能匹配-" + m.group())

# 例5: 匹配小数点
print('----------------------------')
bt = "3.14"
pi_bt = "3\.14"  #表示字面量的点号 （dec.point）

m = re.match(bt, '3.14')    #点号匹配
if m is not None:
    print("3.14能匹配-" + m.group())


m = re.match(pi_bt, '3.14')  #精确匹配
if m is not None:
    print("精确匹配-" + m.group())


m = re.match(bt, '3014')    #点号匹配0
if m is not None:
    print("3014能匹配-" + m.group())


#结果：
# 3.14能匹配-3.14
# 精确匹配-3.14
# 3014能匹配-3014
# 例6： 使用字符集"[ ]"
print('-----')
bt = "[cr][23][dp][o2]"

m = re.match(bt, 'c3po')    #点号匹配
if m is not None:
    print("c3po能匹配-" + m.group())


#结果：
# c3po能匹配-c3po
# 
# 
'''
例7: 重复、特殊字符

正则表达式: \w+@\w+.com可以匹配类似nobody@xxx.com的邮箱地址，
但是类似nobody@xxx.yyy.aaa.com的地址就不能匹配了。
这时候我们可以使用*
操作符来表示该模式出现零次或者多次：\w+@(\w+.)*\w+.com
'''

# 例8: 分组
# 
# group()可以访问每个独立的子组
# groups()获取一个包含所有匹配子组的元组
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())
print( m.group(1))
print( m.group(2))
print( m.groups())
# abc-123
# abc
# 123
# ('abc', '123')
# 例9: 匹配字符串起始和结尾
m = re.search('^the','the end.')
print(m.group())

'''
2.使用findall()、finditer()查找每一次出现的位置
final() 以列表的形式返回所有能匹配的结果
'''
print('-------------')
print(re.findall('car', 'car sscare carrrrrr'))

# finaliter()
# 返回一个顺序访问每一个匹配结果（Match对象）的迭代器
s = 'this and That'
# print(re.finditer(r'(th\w+) and (th\w+)',s, re.I).next().group(1))
# print(re.finditer(r'(th\w+) and (th\w+)',s, re.I).next().group(2))

# 3.使用sub()和subn()搜索和替换
'''
两个函数都可以实现搜索和替换功能，
将某字符串中所有匹配正则表达式的部分进行某种形式的替换。
不同点是subn()还返回一个表示替换了多少次的总数，
和返回结果一起以元组的形式返回
'''
print(re.sub('[ae]','X','abcdef'))
print(re.subn('[ae]','X','abcdef'))
'''
XbcdXf
('XbcdXf', 2)
'''

# 例如：将美式日期MM/DD/YY{,YY}格式转换成DD/MM/YY{,YY}格式
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','2/20/91'))

# 4.在限定模式上使用split()分隔字符串
'''
re模块的split（）可以基于正则表达式的模式分隔字符串。
但是当处理的不是特殊符号匹配多重模式的正则表达式时，
re.split()和str.split()的工作方式相同
'''
print(re.split(':', 'str1:str2'))
v = 'str1:str2'.split(':')
print(v)
# ['str1', 'str2']
# ['str1', 'str2']
# 但当处理复杂的分隔时，
# 就需要比普通字符串分隔更强大的处理方式,
# 例如下面匹配复杂情况
# 当一个空格紧跟在5个数字或2个字母后面时就用split语句分隔
DATA = ('Mountation View, CA 94040', 'sunnyvale, CA', 'Los Altos, 94023', 'Palo Alto CA','Cupertino 95014')
for datum in DATA: 
	print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ',datum))

'''
5.扩展符号
通过使用(?iLmsux)系列选项，
可以直接在正则表达式里面指定一个活着多个标记。
以下是使用re.I/IGNORECASE的示例，
第二个是使用re.M/MULTILINE实现多行混合
'''
m = re.findall(r'(?i)yes','yes? Yes. YES!!!')
print(m)
m = re.findall(r'(?i)th\w+','The quickest way is through this tunnel.')
print(m)


m = re.findall(r'(?im)(^th[\w ]+)', """
This is the first,
another line,
that line,
it's the best
""")
print(m)

# 下一个例子用来演示re.S/DOTALL，
# 该标记表示点号（.）能够用来表示\n符号
m = re.findall(r'th.+',"""
... The first line
... the second line
... the third line
... """)
print(m)#['the second line\n... the third line\n... ']

m = re.findall(r'(?s)th.+',"""
... The first line
... the second line
... the third line
... """)
print(m)#['the second line\n... the third line\n... ']

# re.X/VERBOSE标记允许用户通过抑制在
# 正则表达式中使用空白符来创建更易读的正则表达式
m = re.search(r'''(?x)
\((\d{3})\) #区号
[ ]  #空白符
(\d{3}) #前缀
-  #横线
(\d{4}) #终点数字
''','(800) 555-1212').groups()
print(m)

'''
(?:...)符号可以对部分正则表达式进行分组，
但是不会保存该分组用于后续的检索或应用。
'''
m = re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
print(m)

m =  re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212').groupdict()
print(m)

'''
可以同时使用(?P<name>)和(?P=name)符号。
前者通过使用一个名称标识符而不是使用
从1开始增加到N的增量数字来保存匹配，
如果使用数字来保存匹配结果，
我们就可以通过使用\1、\2、...,来索引，
如下所示，可以使用一个类似风格的\g<name>来检索它们。
'''
m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212')
print(m)
# 
# 使用后者，
# 可以在同一个正则表达式中重用模式。
# 例如，验证一些电话号码的规范化
print(bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)', '(800) 555-1212 800-555-1212 18005551212')))
# 使用（？x）使代码更易读：
b = bool(re.match(r'''(?x)
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
[ ]
(?P=areacode)-(?P=prefix)-(?P=number)
[ ]
1(?P=areacode)(?P=prefix)(?P=number)
''','(800) 555-1212 800-555-1212 18005551212'))
print(b)

'''
可以使用(?=...)和(?!...)符号在目标字符串中实现一个前视匹配：

(?=...)字符串后面跟着...才适配
'''
m=re.findall(r'\w+(?= van Rossum)',
'''
Guido van Rossum
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger
''')

print(m)
# (?!...)字符串后面不跟着...才适配
m = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
'''
	sales@phptr.com
	postmaster@phptr.com
	eng@phptr.com
	noreply@phptr.com
	admin@phptr.com
''')
print(m)#['sales', 'eng', 'admin']

# 比较re.findall()和re.finditer()
vl = ['%s@awcom' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
'''
	postmaster@phptr.com
	noreply@phptr.com
	admin@phptr.com
	eng@phptr.com
	sales@phptr.com
''')]
print(vl)#['admin@awcom', 'eng@awcom', 'sales@awcom']

# 条件正则表达式匹配，
# 假定拥有一个特殊字符，它仅仅包含字母x和y，
# 两个字母必须由一个跟着另外一个，
# 不能同时拥有相同的两个字母
print('---------------------------------------')
b = bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy'))
print(b)#True
print(re.findall(r'(?:(x)|y)(?(1)y|x)', 'xy'))#['x']