# url不仅可以是一个字符串，
# 例如:http://www.baidu.com。
# url也可以是一个Request对象，
# 这就需要我们先定义一个Request对象，
# 然后将这个Request对象作为urlopen的参数使用
from urllib import request
if __name__ == '__main__':
	req = request.Request('http://fanyi.youdao.com')
	res = request.urlopen(req)