'''
    元组 就是像一个括号列表
'''
unit = (0,12,3,445)
print(unit)#(0, 12, 3, 445)


'''
    可以像数组一样获取他的索引值
'''
print(unit[2])#3

'''
    可以获取元组的长度
'''
print(len(unit))#4


'''
    不可以像数组一样的修改元组的值
'''

# unit[0] = 5
# print(unit) 会报错 TypeError: 'tuple' object does not support item assignment



