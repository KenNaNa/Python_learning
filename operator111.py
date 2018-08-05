from __future__ import division
class Operator(object):
	def __init__(self):
		self.obj = {}


	def add(self,*args):
		sum = 0
		self.obj['add'] = {}
		self.obj['add']['arr'] = []
		if len(args) == 1:
			return args[0]
		elif len(args) >= 2:
			 for x in args:
			 	if isinstance(x,(int,float)):
			 		sum += x
			 	else:
			 		self.obj['add']['arr'].append(x)
		return sum

	def multi(self,*args):
		y = 1
		self.obj['multi'] = {}
		self.obj['multi']['arr'] = []

		if len(args) == 1:
			return args[0]
		elif len(args) >= 2:
			for x in args:
			 	if isinstance(x,(int,float)):
			 		y *= x
			 	else:
			 		self.obj['multi']['arr'].append(x)
		return y


	def subb(self,*args):
		y = 0
		self.obj['subb'] = {}
		self.obj['subb']['arr'] = []

		if len(args) == 1:
			return args[0]
		elif len(args) >= 2:
			for x in args:
			 	if isinstance(x,(int,float)):
			 		y -= x
			 	else:
			 		self.obj['subb']['arr'].append(x)
		return y


	def divi(self,*args):
		y = 1
		self.obj['divi'] = {}
		self.obj['divi']['arr'] = []

		if len(args) == 1:
			return args[0]
		elif len(args) >= 2:
			for x in args:
			 	if isinstance(x,(int,float)):
			 		if x == 0:
			 			continue
			 		else:
			 			y /= x
			 	else:
			 		self.obj['divi']['arr'].append(x)
		return y



a = Operator()
print(a.add(1))

print(a.add(1,2,3,4,'a'))
print(a.obj['add']['arr'])