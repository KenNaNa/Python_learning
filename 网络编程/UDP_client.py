import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
for data in [b'Micheal',b'Tracy',b'Sarah',b'Ken']:
	# 发送数据
	s.sendto(data,('127.0.0.1',8080))
	# 接收数据
	print(s.recv(1024).decode('utf-8'))
s.close()