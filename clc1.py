def clc1(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

a = clc1(1,2,3,4)
print(a)
#我们把函数的参数改为可变参数


num = [1,2,34]
print(clc1(num[0],num[1],num[2]))

c = [12,3,4,55]
print(clc1(*c))