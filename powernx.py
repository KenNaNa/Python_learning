x = input('请输入参数x ')
n = input('请输入参数n ')
x = float(x)
n = float(n)
def powernx(x,n):
	if not (isinstance(x,(int,float)) and isinstance(n,(int,float))):
		raise TypeError('TypeError')
	else:
		s = 1
		while n>0:
			n=n-1
			s = s*x
		return s
y = powernx(x,n)
print(y)