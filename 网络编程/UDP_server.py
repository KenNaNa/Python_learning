import socket
# 先创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
s.bind(('127.0.0.1',8080))
print('Bind UDP on 8080...')

while True:
	# 接受数据
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data , addr)
	# recvfrom()方法返回数据和客户端的地址与端口
	# 接收到数据后，直接用sendto()就可以把数据
	# 用UDP协议发给客户端了