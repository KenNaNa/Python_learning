from collections import deque
'''
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
'''

'''
保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
在多行上面做简单的文本匹配，并只返回在前 N 行中匹配成功的行：
'''

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)
        if __name__ == '__main__':
            with open(r'../../cookbook/somefile.txt') as f:
                for line, prevlines in search(f, 'python', 5):
                    for pline in prevlines:
                        print(pline, end='')
                    print(line, end='')
                    print('-' * 20)
'''
我们在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数，也就是
我们上面示例代码中的那样。这样可以将搜索过程代码和使用搜索结果代码解耦。如
果你还不清楚什么是生成器，请参看 4.3 节。
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
且这个队列已满的时候，最老的元素会自动被移除掉。
'''
q = deque(maxlen=3)

print(q)