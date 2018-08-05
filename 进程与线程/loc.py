'''
多线程和多进程最大的不同在于，
多进程中，同一个变量，
各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，
把内容给改乱了
'''

import time , threading
balance = 0
def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(10000):
		change_it(n)


t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
