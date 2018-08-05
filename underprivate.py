class Student(object):  
	def __init__(self,name,age):
		#给属性加上双下划线表示这个属性只能在类的内部访问
		self.__name = name
		self.__age = age
		self.sex = 'Man'
	def print_name_age(self):
		print((self.__name,self.__age))
		print(self)

	def getName(self):#获取内部姓名
		return self.__name

	def getAge(self):#获取内部年龄
		return self.__age

	def getSex(self):#获取性别
		return self.sex

	def changeName(self,name):#定义一个可以从外部改变姓名的函数
		self.__name = name
		print('姓名已改变')

	def changeAge(self,age):#定义一个可以从内部改变年龄的函数
		self.__age = age
		print('年龄已改变')


	def changeSex(self,sex):
		self.sex = sex
		print('性别已改变')

	def addPerpoty(self,**dicta):
		if 'name' in dicta:
			self.__name = dicta['name']
		if 'age' in dicta:
			self.__age = dicta['age']
		if 'sex' in dicta:
			self.sex = dicta['sex']






student = Student('Ken',20)
print(type(student))
student.print_name_age()
print(student.getAge())
print(student.getName())
print(student.getSex())
print(Student.__init__)
print(student.__init__)
print(student)
student.changeAge(21)
student.changeName('Tom')
student.changeSex('Woman')
print(student.getAge())
print(student.getName())
print(student.getSex())
d = {'name':'Susan','age':20,'sex':'Man'}
student.addPerpoty(**d)
student.print_name_age()
print(student.getAge())
print(student.getName())
print(student.getSex())
# print(student.name,student.age,student.__age,student.__name)
#上面注释的会报错