def add_end(L=None):#定义默认参数要牢记一点：默认参数必须指向不变对象！
    if L is None:
        L = []
    L.append('END')
    return L
a = add_end()
print(a)