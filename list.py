num_list = [1,2,3]
num_list1 = [5,6,7]
print(num_list)


print(num_list[2])#可以读取
print(num_list1[2])

num_list[2] = 4#可以写
num_list1[2] = 8
print(num_list)
print(num_list1)


print(len(num_list))#可以读出长度


#可以拼接数组
print([num_list,num_list1])#[[1, 2, 4], [5, 6, 8]]


#可以这样索引 index:other index
num_list2 = [1,2,3,4,5,5,6]
print(num_list[2:6])#[4]
print(num_list2[2:6])#[2:6]这个索引方式跟matlab有点相似
print(num_list2[-2:-1])#输出的是[5]
print(num_list2[-7])#1
'''
    可以总结为从左到右索引的话索引值为0开始
    如果是从又到左的话 -1到-length
'''


'''
    添加到元素列表后面
    的方式
    append()
'''
list = [1,2,3,4,5]
list.append(6)
print(list.append(6))#返回的是none
print(list)#[1, 2, 3, 4, 5, 6, 6]


'''
    从列表的后面删除元素
    del list[7]
'''

list1 = [1,2,3,4,5]
del list1[3]
print(list1)#[1, 2, 3, 5]

'''
    列表中元素的算术
    两个两相加是指将后一个列表的元素连接在前一个列表的元素的后面
'''

num = [1,2,33,4]
num1 = [5,6,7,8]

print(num + num1)#[1, 2, 33, 4, 5, 6, 7, 8]

print(num*5)#[1, 2, 33, 4, 1, 2, 33, 4, 1, 2, 33, 4, 1, 2, 33, 4, 1, 2, 33, 4]

#print(num / 5)#会报错

#print(num / num1)#会报错

#print(num * num1)#会报错

#print(num - num1)#会报错

#print(num + 50)#会报错

