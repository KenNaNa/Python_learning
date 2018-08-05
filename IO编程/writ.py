f = open('C:/Users/Administrator/Desktop/html/Python/IO编程/test.txt','w',encoding='utf-8',errors='ignore') 
f.write('hello world')

f.close()

with open('C:/Users/Administrator/Desktop/html/Python/IO编程/test.txt','r',encoding='utf-8',errors='ignore') as f:
	print(f.read())


with open('C:/Users/Administrator/Desktop/html/Python/IO编程/test.txt','a',encoding='utf-8',errors='ignore') as f:
	f.write('  welcome to python world')


with open('C:/Users/Administrator/Desktop/html/Python/IO编程/test.txt','r',encoding='utf-8',errors='ignore') as f:
	data = f.read()
	print(data)