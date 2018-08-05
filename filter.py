'''
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(x):
	return x % 2 == 1
odd_num = list(filter(is_odd,[1,2,3,4,5,6,78,9]))
print(odd_num)

#去除空字符串
def not_empty(s):
	return s and s.strip()
not_str = filter(not_empty,['ken','ye','wei','lin',''])
print(not_str)
print(list(not_str))