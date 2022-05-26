import random


def qudian():
    x=int(10*random.random())
    y=int(10*random.random())
    return x,y
print('10个点的坐标是：')
ls=[]
lt=[]
for i in range(10):
    j=qudian()
    if i!=4 and i!=9 :
        print(j,end="")
        ls.append(j)
    else:
        print(j)
        ls.append(j)
d=0
for i in ls:
    for j in ls:
        distance=(((j[0]-i[0])**2)+((j[1]-i[1])**2))**0.5
        if distance>=d:
            d=distance
            lt.append(i)
            lt.append(j)
e=lt[-1]
f=lt[-2]
print('距离最大的两个点：{}{}'.format(e,f))