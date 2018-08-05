# -*- coding: utf-8 -*-
x = input()#因为输入的参数为字符串
x = float(x)#所以需要转换
def my_abc(x):
	if x >= 0:
		print('您输入的变量大于零')
	else:
		print('您输入的变量没有大于零')
my_abc(x)