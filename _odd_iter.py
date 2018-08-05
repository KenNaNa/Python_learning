#用来产生一个无限奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

#用过滤出
def _not_shu(n):
	return lambda x:x % n > 0
#最后，定义一个生成器，不断返回下一个素数
def _primes():
	yield 2
	it = _odd_iter()#用来初始化序列
	while True:
		n = next(it)#取出序列的第一个数
		yield n
		it = filter(_not_shu(n),it)

for val in _primes():
	if val < 1000:
		print(val)
	else:
		break