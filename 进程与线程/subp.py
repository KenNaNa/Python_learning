'''
很多时候，子进程并不是自身，
而是一个外部进程。
我们创建了子进程后，
还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，
然后控制其输入和输出
'''

import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''
$ nslookup www.python.org
服务器:  cache-b.guangzhou.gd.cn
Address:  202.96.128.166

非权威应答:
名称:    python.map.fastly.net
Addresses:  2a04:4e42:36::223
          151.101.228.223
Aliases:  www.python.org

Exit code: 0
'''
# 如果子进程还需要输入，
# 则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output)
print(err)
# print(output.decode('utf-8'))
print('Exit code:', p.returncode)