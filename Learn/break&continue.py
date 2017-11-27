for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 循环可以有一个`else`子句：它在虚幻迭代完整个列表（对于for）或执行条件false（对于while）时执行，但循环被break终止的情况下不会执行。

for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found a number', num)