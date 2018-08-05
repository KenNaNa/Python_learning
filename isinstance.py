x = input()
x = int(x)
def my_abc(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type');
	if x>=0:
		print(x)
	else:
		print(abs(x))


my_abc(x)