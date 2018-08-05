from urllib import request

if __name__ == '__main__':
	url = 'http://www.fanyi.baidu.com/'
	req = request.urlopen('http://www.python.org')
	data = req.read()
	html = data.decode('utf-8')
	with open('urllib_test02.html','w',encoding='utf-8') as f:
		f.write(html)
