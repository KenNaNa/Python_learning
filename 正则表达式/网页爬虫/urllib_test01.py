from urllib import request
url = 'http://www.baidu.com'
req = request.urlopen(url)
html = req.read().decode('utf-8')
with open('urllib_test01.html','w',encoding='utf-8') as f:
	f.write(html)
'''
 urllib使用使用request.urlopen()打开和读取URLs信息，
 返回的对象response如同一个文本对象，
 我们可以调用read()，
 进行读取。再通过print()，将读到的信息打印出来
'''
print(req)