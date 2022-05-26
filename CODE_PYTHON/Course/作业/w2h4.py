a = int(input("请输入第一条边"))
b = int(input("请输入第二条边"))
c = int(input("请输入第三条边"))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print("由 a、b、c构成的三角形面积为:{:.2f}".format(s))
