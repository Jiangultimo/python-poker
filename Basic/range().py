for i in range(5):
    print(i)

#range() 函数会生成一个等差级数链表

#尝试打印 len(range(5))
print(len(range(5))) # 正常输出 5


for a in range(0, 10, 2):
    print(a)

lists = ['Mary', 'had', 'a', 'little', 'lamb']
for b in range(len(lists)):
    print(b, lists[b])

# 打印一个序列
print(range(10))

# 迭代器 for , list
# 序列和列表是两种不同的概念，列表就是数组
# 其中list迭代序列range生成一个列表
print(list(range(10))) # 打印为一个序列
for c in list(range(10)):
    print(c)
