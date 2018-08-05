class Set(object):
	#首先有一个集合
	def __init__(self):
		self.items = {}

	#定义一个判断元素是否存在的方法
	def has(self,key):
		return key in self.items

	#定义一个可以向集合添加元素的方法
	def add(self,key,value):
		if not self.has(key):
			self.items[key] = value
			return True
		else:
			return False

	#定义一个可以删除集合中的元素的方法
	def remove(self,key):
		if self.items[key]:
			del self.items[key]
			return True
		else:
			raise ValueError('你删除的属性不存在')

	#定义一个清除集合元素的方法
	def clear(self):
		self.items = {}

	#定义一个计算集合的属性键的长度
	def size(self):
		return len(self.items.keys())

	def sizeLegacy(self):
		count = 0
		for key in self.items:
			if self.has(key):
				++count
		return count

	#定义一个values方法
	def values(self):
		valueArr = []
		for key in self.items:
			valueArr.append(self.items[key])
		return valueArr

	def valuesLegacy(self):
		return self.items.keys()

	#定义一个keys()方法
	def keys(self):
		keysArr = []
		for key in self.items:
			keysArr.append(key)
		return keysArr

	#定义一个getitems
	def items(self):
		return self.items;


	#并集
	def union(self,otherSet):
		unionSet = Set()
		thisValues = self.values()
		thisValuesLength = len(thisValues)

		otherValues = otherSet.values()
		otherValuesLength = len(otherValues)

		#自身查重
		for i in range(0,thisValuesLength):
			for j in range(0,thisValuesLength-i-1):
				if thisValues[i]!=thisValues[j]:
					continue
				else:
					thisValues.pop(thisValues[i])
					thisValuesLength = thisValuesLength - 1

		for i in range(0,otherValuesLength):
			for j in range(0,otherValuesLength-i-1):
				if otherValues[i]!=otherValues[j]:
					continue
				else:
					otherValues.pop(otherValues[i])
					otherValuesLength = otherValuesLength - 1
		#循环比较，去重复的元素
		for i in range(0,thisValuesLength):
			for j in range(0,otherValuesLength):
				if thisValues[i]!=otherValues[j]:
					unionSet.add(str(thisValues[i]),thisValues[i])
					unionSet.add(str(otherValues[j]),otherValues[j])
				else:
					unionSet.add(str(thisValues[i]),thisValues[i])

		return unionSet

	#交集
	def intersection(self,otherSet):
		interSet = Set()
		interSetValue = interSet.values()
		otherSetValue = otherSet.values()
		otherSetValueLength = otherSetValue.length
		interSetValueLength = interSetValue.length
		for i in range(0,otherSetValueLength):
			if otherSet.has(str(otherSetValue[i])):
				interSet.add(str(otherSetValue[i]),otherSetValue[i])

		return interSet

	#差集
	def diff(self,otherSet):
		diffSet = Set()
		thisValue = self.values()
		thisValueLength = thisValue.length

		otherValue = otherSet.values()

		for i in range(0,thisValueLength):
			if not otherSet.has(str(thisValue[i])):
				diffSet.add(str(thisValue[i]),thisValue[i]);
		
		return diffSet

	#求子集
	def subset(self,otherSet):
		if self.size()>otherSet.size():
			return None
		else:
			thisValue = self.values()
			thisValueLength = thisValue.length
			b = True
			thisArr = []
			for i in range(0,thisValueLength):
				if not otherSet.has(thisValue[i]):
					b = b and False
				else:
					b = b and True
			if b  :
				return self
			else:
				return None







s = Set()
s.add("Ken",20)
print(s.keys())
print(s.values())
s.clear()
print(s.keys())

