#给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
	def __init__(self,name,id,sex):
		self.name = name
		self.id = id
		self.sex = sex
	def getName(self):
		return self.name

	def getId(self):
		return self.id

	def getSex(self):
		return self.sex

st = Student('Ken',20150101010009,'Boy')

print(st.getId())
print(st.getName())
print(st.getSex())
st.score = 99#给你99分，怕你骄傲，继续加油哦

print(st.score)

del st.name
print(st.name)#删掉之后，程序运行就会出错
'''
小结

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''
