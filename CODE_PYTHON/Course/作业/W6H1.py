def DrawPic(n,char):
    for i in range(0,n):
        print(" "*(n-i-1)+char*(2*i+1))
    for i in range(0,n):
        print(" "*(i+1)+char*(2*(n-i-1)-1))
n=eval(input("请输入一个整数："))
char=input("请输入一个字符：")
DrawPic(n,char)