'''
正常情况下，当我们定义了一个class，
创建了一个class的实例后，
我们可以给该实例绑定任何属性和方法，
这就是动态语言的灵活性。先定义class
'''

class Obj(object):
	pass

Obj.name = 'Obj'
def set_age(self,age):
	self.age = age

from types import MethodType

obj = Obj()
obj.name = 'obj'
obj.set_age = MethodType(set_age,obj)#给实例添加一个方法

obj.set_age(24)
print(obj.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的

# print(obj2.age)#会包属性错误
# 为了给所有实例都绑定方法，可以给class绑定方法
Obj.set_age = set_age
obj2 = Obj()
obj2.set_age(20)
print(obj2.age)
#通常情况下，上面的set_score方法可以直接定义在class中，
#但动态绑定允许我们在程序运行的过程中动态给class加上功能，
#这在静态语言中很难实现
#使用__slots__
#为了达到限制的目的，Python允许在定义class的时候，
#定义一个特殊的__slots__变量，
#来限制该class实例能添加的属性
class Student(object):
	__slots__ = ('name','age')#给这类限制了两个属性
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

st = Student('Jim',20)
st.name = 'Ken'
st.age = 20
# st.sex = 'Man'#报错了
print(st.name)
print(st.age)

print(st.getAge())
print(st.getName())
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
#对继承的子类是不起作用的
#
print('--------------------------------')
class S(Student):
	pass

s = S('name',20)
s.sex = 'Man'
s.name = "jim"
s.age = 20
print(s.sex)
print(s.getName())
print(s.getAge())
print(s.age)
print(s.name)
