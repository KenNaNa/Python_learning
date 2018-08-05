import os
print(os.name)#'nt'表示windows系统
# 如果是Linux，UNIX，mac系统的话就打出‘posix’
# 获取详细的系统信息
# print(os.uname())注意uname()函数在Windows上不提供，
# 也就是说，os模块的某些函数是跟操作系统相关的
# 获取环境变量
print(os.environ)
print(os.environ.get('PATH'))

print(os.environ.get('x', 'default'))

print(os.path.abspath('.'))

print(os.path.join('C:/Users/Administrator/Desktop/html/Python/', 'testdir'))
# os.mkdir('C:/Users/Administrator/Desktop/html/Python/IO编程/img')

print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('C:/Users/Administrator/Desktop/html/Python/a.html'))

# os.rename('ose.py','ose1.py')
# os.remove('ose1.py')

v = [x for x in os.listdir('.') if not os.path.isdir(x)]
print(v)

v = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(v)

print(os.getcwd())#获取当前文件的路径