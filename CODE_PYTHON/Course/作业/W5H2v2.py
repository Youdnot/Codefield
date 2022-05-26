import random

def GetRandomChar(a):
    for i in range(int(a)):
        ran = int(62*random.random())
        if ran >= 0 and ran <= 9:
            print(ran,end="")
        elif ran >= 10 and ran <= 35:
            print(chr(ran-10+ord('A')),end="")
        else:
            print(chr(ran-36+ord('a')),end="")

b = int(input("请输入一个整数："))
if b >= 5 and b <= 10:
    GetRandomChar(b)   
else:
    print("请输入五到十之间的整数")