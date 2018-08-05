import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()#在windows下没有fork功能
if pid==0:
	print('I am child process (%s) and my parent is %s' %  % (os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
print(pid)
'''
在Linux，UNIX，Mac系统下运行结果为
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''
'''
有了fork调用，一个进程在接到新任务时就可以
复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，
每当有新的http请求时，
就fork出子进程来处理新的http请求
'''