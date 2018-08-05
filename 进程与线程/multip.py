from multiprocessing import Process

import os

# 启动一个子进程并等待其结束
def run_proc(name):
	print('Run child processing %s (%s)' % (name,os.getpid()))


if __name__ == '__main__':
	print('Parent Process %s' % os.getpid())
	p = Process(target=run_proc,args=('test',))
	print('Child Process will running .')
	run_proc('Jim')
	p.start()#同来启动进程
	p.join()#用来结束进程
	print('child process is ending')

	
