import random

def GetRandomChar(a):
    for i in range(int(a)):
        ran1 = int(3*random.random()+1)
        if ran1 == 1:
            p1 = int(10*random.random()+1)
            print(p1,end="")
        elif ran1 == 2:
            p2 = int(24*random.random()+1)
            print(chr(p2+ord('A')),end="")
        else:
            p3 = int(24*random.random()+1)
            print(chr(p3+ord('a')),end="")

b = int(input("请输入一个整数："))
if b >= 5 and b <= 10:
    GetRandomChar(b)   
else:
    print("请输入五到十之间的整数")