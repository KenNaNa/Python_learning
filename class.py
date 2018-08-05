class Student(object):
	# print(self)会报错
	def __init__(self,name,age):
		print(self)
		self.name = name
		self.age = age
	def getCode(self):
		if self.age<18:
			print('是青少年')
		elif self.age>18 and self.age<45:
			print('是壮年人')
		elif self.age>45 and self.age<60:
			print('是中年人')
		else:
			print('是老年人')
	pass

print(Student)
student = Student("Ken",20)
student.name = 'Ken'
student.age = 20
student.sex = 'man'
print(student)
print(student.age)
student.getCode()

'''
如果要让内部属性不被外部访问，
可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，
就变成了一个私有变量（private），
只有内部可以访问，
外部不能访问
'''