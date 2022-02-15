s=input("请输入一个字符串")
n=0
a=''
for i in s:
    if s.count(i)>n:
        n=s.count(i)
        a=i
    else:
        continue
print("出现次数最多的字符是：{}".format(a))