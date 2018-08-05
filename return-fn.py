'''
高阶函数除了可以接受函数作为参数外，
还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。
通常情况下，求和的函数是这样定义的
'''
#不定参跟javascript的...args太像了
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

ax = calc_sum(1,2,3,4,5)
print(ax)


#如果不想码上计算出来
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

lazysum = lazy_sum(1,2,3,4,5,6)
print(lazysum)
print(lazysum())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力
'''

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1==f2)#false
#f1()和f2()的调用结果互不影响。
#注意到返回的函数在其定义内部引用了局部变量args，
#所以，当一个函数返回了一个函数后，
#其内部的局部变量还被新函数引用，
#所以，闭包用起来简单，实现起来可不容易
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())#9
print(f2())#9
print(f3())#9
#这一点跟javascript的闭包
#for(var i=0;i<10;i++){}
#返回闭包时牢记一点：
#返回函数不要引用任何循环变量，
#或者后续会发生变化的变量
#
def count():
	fs = []
	for i in range(1,4):
		n = i
		def f():
			return n * n
		fs.append(f)
	return fs 
print(f1())#9
print(f2())#9
print(f3())#9

'''
跟javascript的闭包太像了
function count(){
	var fs = []
	for( var i=0;i<10;i++ ){
		(function(i){
			fs.push(function(){
				return i * i
			})
		})(i)
	}
}
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs