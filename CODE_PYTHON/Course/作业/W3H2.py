a = eval(input("请输入一个十进制整数:"))
p = ""
while a>0:
    p = p + str(a%2)
    a=a//2
    
print(p[::-1])
