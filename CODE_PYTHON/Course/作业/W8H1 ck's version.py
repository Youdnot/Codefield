import random
ls=[]
for i in range(50):
    a=random.randint(1,999)
    ls.append(a)
print(ls)
c=1000
lb=0
n=-1
for b in range(50):
    c=1000
    for i in ls:
        n=n+1
        if lb<=i<=c:
            c=i
            ls[b],ls[n]=ls[n],ls[b]
    
    lb=ls[b]
    
    
print(ls)