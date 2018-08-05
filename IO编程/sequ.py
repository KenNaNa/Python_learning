d = dict(name='Bob', age=20, score=88)
#{'name': 'Bob', 'age': 20, 'score': 88}
print(d)
print(d.items())
for k,v in d.items() :
	print(k,v)
class Dict(dict):
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)

	def __getattr__(self,key):
		return self[key]

	def __setattr__(self,key,value):
		self[key] = value

def dict(**kw):
	obj = {}

	for k,v in kw.items():
		obj[k] = v

	return obj

print(dict(name='Bob', age=20, score=88))

print('--------------------------------------')

d = dict(name='Bob', age=20, score=88)

v = Dict(name='Bob', age=20, score=88)['name']

print(v)

import pickle

print('-------------------------------------')
d = dict(name='Bob', age=20, score=88)
v = pickle.dumps(d)
print(v)

c = pickle.loads(v)
print(c)
print('----------------------------------')
with open('dump.txt','wb') as f:
	pickle.dump(d,f)

with open('dump.txt','rb') as f:
	v = pickle.load(f)
	print(v)

print('---------------------------------')
import json
d = dict(name='Bob', age=20, score=88)
v = json.dumps(d)
print(v)


print('--------------------------------')
json_str = '{"name": "Bob", "age": 20, "score": 88}'
v = json.loads(json_str)

print(v)

print('----------------------------------------')
# d = {"name": "Bob", "age": 20, "score": 88}
# with open('json.txt','wb') as f:
# 	json.dump(d,f)

# with open('json.txt','rb') as f:
# 	v = json.load(f)
# 	print(v)
# json.dump()
# JSON进阶
# 可以通过创建类来初始化JSON
class Student(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

s = Student('Ken',20,'Man')

def student2dict(std):
	return {
		"name" : std.name,
		"age" : std.age,
		"sex" : std.sex
	}
print(json.dumps(s, default=student2dict))
