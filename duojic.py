# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能
'''
Dog - 狗狗；
Bat - 蝙蝠；
Parrot - 鹦鹉；
Ostrich - 鸵鸟。
'''
class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass


class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，
# 只需要先定义好Runnable和Flyable的类

class Runnable(object):
	def run(self):
		print('running !')

class Flyable(object):
	def fly(self):
		print('flying !')

class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Runnable):
	pass

class Parrot(Bird,Flyable):
	pass

class Ostrich(Bird,Flyable):
	pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
'''
MixIn
在设计类的继承关系时，
通常，主线都是单一继承下来的，
例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，
通过多重继承就可以实现，
比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
这种设计通常称之为MixIn
'''

