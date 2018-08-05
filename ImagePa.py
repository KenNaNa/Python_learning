# _*_ coding:utf-8 _*_
# import re

# import base64
import re
# import enum
# from types import MappingProxyType, DynamicClassAttribute
# import functools as _functools
# from collections import namedtuple
from urllib import request
import urllib.parse
# http://image.baidu.com/
# 首先我们从这个网址获取网页代码
# 首先要通过URLlib打开这个网页
# 获取网页代码
# 然后通过正则匹配获取img标签中src中的连接
# 通过这些链接下载图片


def getHtml(url):
	page = request.urlopen(url)
	html = page.read().decode('utf-8')

	return html

def getImgSrc(html):
	x = 1
	path = 'C:/Users/Administrator/Desktop/html/Python/img/'
	reg = r'src="(.*?\.jpg)" style'
	srcReg = re.compile(reg)
	srcList = re.findall(srcReg,html)
	for imgSrc in srcList:
		request.urlretrieve(imgSrc,path + '%s.jpg' % x)#
		x += 1
		if x > 10:
			break
	print(srcList) 

# print(getHtml("https://tieba.baidu.com/f?ie=utf-8&kw=%E5%9B%BE%E7%89%87&fr=search"))
html = getHtml("https://tieba.baidu.com/p/1433290786#!/l/p1")
getImgSrc(html)