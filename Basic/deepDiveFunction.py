# 默认参数
def ask_ok( prompt, retries = 4, complaint = 'Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print(ok)
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        print(retries)
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

# 多种传参调用方式
ask_ok('Do you really want to quit?')
ask_ok('Ok to overwrite the file?', 2)
ask_ok('Ok to overwrite the file?', 2, 'Come on, only yes or no!')

# 默认值在函数 ***定义作用域*** 被解析:
i = 5
def f(arg = i):
    print(arg)

i = 6
print(i) # 6
f() # 打印 5

# 默认肤质只能被赋值一次，多次赋值将会累积传入的参数，如果不想在后续调用中累积，可以这样：
def g(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l

# 关键字参数
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("this parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the ", type)
    print("--it's", state, '!')
# 在调用中，关键字的参数必须跟随在为止参数的后面。
# 传递的所有关键字参数必须与含糊接受的某个参数相匹配， 顺序不重要
# 感觉这里应该类比ES6的参数默认值以及解构

# 字典，元组
# 通过代码可以推敲一下，元组就是没有关键字，没有名字的参数
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind)
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)

    print('-'*40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
# 调用
cheeseshop("Linmurger", "It's very runny, sir",
           "It's really very, VERY runny, sir.",
           shopkeeper = "Michael Palin",
           clinet = "John Cleese",
           sketch = "Cheese Shop Sketch")

# Lambda 形式
# 通过Lamda关键字，可以创建短小的匿名函数。
# Lambda形式可以踊跃人格需要的函数对象，但是语法限制，他们只能有一个单独的表达式。
def make_incrementor(n):
    return lambda x: x+n
f = make_incrementor(42)
f(0) # 42
f(1) # 43

# 另一个用途：将一个小函数作为参数传递：
pairs = [(1,'one'),(2, 'two'),(3,'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

