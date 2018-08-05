def clc(numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

sum = clc([1,2,3,4])
print(sum)
a = (1,2,3,4,5,6)
tip = clc(a)
print(tip)

# c = clc(1,2,3,4)
# print(c)