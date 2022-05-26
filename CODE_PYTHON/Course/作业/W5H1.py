def func(a):
    A = str(a)
    b = 0
    for i in A:
        b += int(i)
    return b

c = int(input("请输入一个整数"))
d = func(c)
print("它的各位数字之和为{}".format(d))