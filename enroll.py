# -*- coding: utf-8 -*-
name = input('请输入name: ')
gender = input('请输入gender: ')
# age = input('请输入age: ')
# address = input('请输入address: ')
def enroll(name,gender,age=18,address='广东'):
	if not (name and gender):
		print('您没有输入')
	else:
		print(name)
		print(gender)
		print(age)
		print(address)
enroll(name,gender,'age','address')


