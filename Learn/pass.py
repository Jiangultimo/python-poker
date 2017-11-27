# pass 语句什么也不做。它用于那些语法上必须要有什么语句，但是程序什么也不做的场合：
while True:
    pass # Busy-wait for keyboard interrupt(ctrl+c)

# 通常用于创建最小结构的类
class MyEmptyClass:
    pass

# 可以创建新代码时用来函数或控制体的占位符
def initlog(*args):
    pass # Remember to implement this!