# -*- coding:utf-8 -*-
import time
f = open('C:/Users/Administrator/Desktop/html/Python/a.html','r')
data = f.read()

print(data)
f.close()

try:
	b = open('txt.txt','r',encoding='utf-8')#
	
except IOError as e:
	print(e)
	if b :
		print(b)
		b.close()

data = b.read()
print(data)
b.close()

try:
    f = open('/path/to/file', 'r')
    print(f.read())
except IOError as e:
	print(e)
finally:
    if f:
    	f.close()


print('-------------------------------------------------------------------------------------')
with open('C:/Users/Administrator/Desktop/html/Python/ImagePa.py','r',encoding='utf-8') as f:
	for x in f.readlines():
		print(x.strip())
print('-------------------------------------------------------------')
with open('C:/Users/Administrator/Desktop/html/Python/img/1.jpg','rb') as f:
	data = f.read()
	print(data)

print('------------------------------------------------------------------------')
with open('C:/Users/Administrator/Desktop/html/Python/IO编程/txt.txt','r',encoding='utf-8') as f:
	for line in f.readlines():
		print(line)
		# time.sleep(1)
print('------------------------------------------------------------------------')
with open('C:/Users/Administrator/Desktop/html/Python/IO编程/txt.txt','r',encoding='utf-8',errors='ignore') as f:
	for line in f.readlines():
		print(line)
		time.sleep(1)

