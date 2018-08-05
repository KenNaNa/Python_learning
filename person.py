def person(name,age,**kw):
	print(name)
	print(age)
	print(kw)


person('Ken',20,Suan=18,Jim=20,Tom=20)
#**kw相当于js中的rest剩余参数
#
#
'''
对于关键字参数，
函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

'''