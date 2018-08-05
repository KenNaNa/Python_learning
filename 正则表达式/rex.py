import re
'''
有了准备知识，我们就可以在Python中使用正则表达式了。
Python提供re模块，包含所有正则表达式的功能。
由于Python的字符串本身也用\转义，所以要特别注意
'''
s = 'ABC\\123'
#当我们在写字符串的时候有特殊字符的，
#都需要加上反斜杠(\)去掉特殊意义
#但是我们引入re模块之后可以在字符串前面加上r
#就可以肆无忌惮的乱写了
s = r'ABC\\-1123'
r = re.match(s,'ABC\-1123')
sp = r.span()
print(sp)#(0,9)
sp = r.span(0)#默认为零
print(sp)
print(r)
print('---------------------------------')
reg = r'^\d{3}\-\d{3,8}$'
s = '010-12345678'
v = re.match(reg,s)
print(v)
c = v.span()
print(c)
# match()方法判断是否匹配，如果匹配成功，
# 返回一个Match对象，否则返回None。常见的判断方法就是
if re.match(reg,s):
	print('您匹配成功了，恭喜')


print('----------------------------')
inp = input('请输入要匹配的文字：')
s = r'Ken'
if re.match(s,inp):
	print('you pass')
else:
	print('you failed')

print('------------------')
# \d匹配
d = r'\d'#匹配数字
s = '1234'
print(re.match(d,s))#匹配到1 
d = r'\d+'#匹配前面的多个字符
print(re.match(d,s))#匹配到1234

d = r'\d.'#.匹配任意字符
print(re.match(d,s))#匹配到12

d = r'\d*'#匹配任意个字符
print(re.match(d,s))#匹配到1234

d = r'\d?'#匹配一个或零个字符
print(re.match(d,s))#匹配到1

d = r'\d{0,}'#匹配0，到n个字符


print(re.match(d,s))#1234


d = r'\d{0,1}'
print(re.match(d,s))#1


# 匹配空格\s
d = r'\s'
s = ' 123'
print(re.match(d,s))

# 匹配数字或字母\w
d = r'\w+'
s = '123w'
print(re.match(d,s))


# []匹配一个字符
d = r'[0-9a-zA-Z_]'
s = '123344'
print(re.match(d,s))

d = r'[0-9a-zA-Z_]+'
print(re.match(d,s))

# |或匹配存在的字符
d = r'(p|P)ython'
s = 'python'
print(re.match(d,s))

# ^匹配以什么开头
d = r'^py'
s = 'python'
print(re.match(d,s))

# $匹配以什么结尾
d = r'[0-9]$'
s = 'fimin1'
print(re.match(d,s))
print(re.search(d,s))
print(re.search(d,s).span())
print(re.search(d,s).group())