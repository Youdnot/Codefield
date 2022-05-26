import random
print("十个点的坐标是:")

lt=[]
for i in range(10):
    t=(random.randint(0,9),random.randint(0,9))    
    lt.append(t)
    if i == 4:
        print(t)
    else:
        print(t,end=' ')
print()
ls=[]
length=0
for i in lt:
    for j in lt:
        l=((i[0]-j[0])**2+(i[1]-j[1])**2)**1/2
        if l>=length:
            length=l
            ls.append(i)
            ls.append(j)

print("距离最大的两个点是{}{}".format(ls[-1],ls[-2]))
