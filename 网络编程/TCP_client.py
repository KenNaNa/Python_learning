# 客户端
# 导入socket库
import socket
# 创建一个socket对象
# 指定相应的协议
# AF_INET是指使用IPv4的IP协议
# SOCK_STREAM使用面向流的TCP协议
# 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
# 建立连接:
s.connect(('127.0.0.1',8080))
# 注意返回的参数是一个tuplel类型，包含IP地址和端口号
# 

# 客户端要主动发起TCP连接，必须知道服务器的端口和IP地址，
# 比如新浪微博的域名可以是www.sina.com.cn自动转换为IP地址
# 但是怎么知道服务器的端口呢
# 答案是，提供什么样的服务，端口是固定下来的
# 由于我们想访问网页，我们必须把端口号固定为80端口
# 因为80端口是web服务的标准端口
# 例如STMP的默认端口为25
# FTP的默认端口为21
# 
# 建立TCP连接后，
# 我们就可以向服务器发送数据了
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: http://0.0.0.0\r\nConnection: close\r\n\r\n')
# TCP连接是创建的是双向通道，双方都可以同时发送数据和接受数据
# 但是谁先发送数据，谁先接受数据呢
# 例如HTTP规定客户端先发送数据给服务器，然后服务器接受数据
# 然后服务器再把请求的数据返回给客户端
# 接下来就是本地服务器返回的数据了
buffer = []
while True:
	# 每次指定接受1K的数据
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

	data = b''.join(buffer)
# 接受数据时
# 调用recv(max)方法
# 一次最多接受指定的字节数
# 因此，while循环必须循环直到数据接受为空
# 才退出循环
# 
# 最后就是关闭连接
s.close()
# 将接收到数据进行分割
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('header.txt','wb') as f:
	f.write(header)
# 写入文件中
with open('d3.html','wb') as f:
	f.write(html)
