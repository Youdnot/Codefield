import random
ori=[]
for i in range(0,50):
    a=random.randint(1,999)
    ori.append(a)
x=0
n=50
for i in range(len(ori)):
    for i in range(n):
        if ori[x] >= ori[x+i]:
            ori[x],ori[x+i]=ori[x+i],ori[x]
        else:
            continue
    n-=1
    x+=1
for i in range(len(ori)):
    if (i+1)%10==0:
        print('{0:>3}'.format(ori[i]))
    else:
        print('{0:>3}'.format(ori[i]),end='  ')