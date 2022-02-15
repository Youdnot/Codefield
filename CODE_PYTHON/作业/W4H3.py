a=ord(input("请输入开始字母"))
b=ord(input("请输入结束字母"))
if a>=b:
    a,b=b,a
c=a
for i in range(a,b+1):
    for i in range(c,b+1):
        print(chr(i),end='')
    for i in range(a,c):
        print(chr(i),end='')
    print()
    c+=1
        
