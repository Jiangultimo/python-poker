def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n"""
    # 添加中间变量
    # result = []
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        # result.append(a
        a, b = b, a+b
    # 返回函数结果
    # return result
    print()

fib(2000)

f = fib
f(100)

print(fib) # 会打印 0x101c61e18 地址
print(fib(0))

# 将结果赋值
f100 = fib(100)
print(f100)

# 关键字 def 引入函数定义
# 函数体的第一行语句可以使可选的字符串文本，这个字符串是函数的文档字符串（docstrings）
# 函数的调用会为函数局部变量生成一个新的符号表。即，所有函数中的变量赋值都是将值存储在局部符号表。变量引用首先在局部符号表中查找，然后是包含函数的局部符号表，然后是全局符号表，最后是内置名字表。
# 我觉得这里类比JavaScript的作用域，从里向外查找
# 函数引用的实际参数在函数调用时引入局部符号表
# 实参总是 传值调用 （值总是一个对象引用，不是对象的值，或许按引用传递说比较好？）
# fib函数没有return语句，但是会返回一个值：None(内建名称)