freg = '欢迎来到python这个快乐的编程世界'
print (freg)
'''
    如果遇到了需要转义的字符的话
    一定要加上反斜杠（\）
    此处是注释内容
    在Python一般用的是
    # \'\'\' 三个逗号
'''
exm = 'why are\'t learn the python'
print(exm)


'''
    在字符串中嵌入值
    我们可用%s
    %s 为 num 的占位符
'''
num = 1000
str = 'I got %s points'
print(str % num)

'''
    一个字符串中可以使用多个
    占位符%s
    占位符的个数要与 对应的内容的个数相等
'''

str2 = 'what did the number %s say to the number %s %s Nice belt'
print(str2 % (0,8,10))

#str3 = 'what did the number %s say to the number %s Nice belt'
#print(str3 %(0,8,10))#会报错

#str3 = 'what did the number %s say to the number %s Nice belt'
#print(str3 %(0))#会报错

'''
    字符串也有除法 乘法
'''

str4 = 10 * 'a'
print(str4)#aaaaaaaaaa


str5 = 'aaaaaaaaaa'
print(str5 * 1/5)#报错