x = input('输入参数x')
x = float(x)
def power(x):
	if not isinstance(x,(int,float)):
		print('TypeError')
	else:
		return x*x
y = power(x)
print(y)