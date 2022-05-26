import random
ori=[]
for i in range(50):
    a=random.randint(1,999)
    ori.append(a)
order=0
n=1000
for x in ori: 
    if x <= n:
        n=x
    else:
        continue
    ori[order]=n
    order+=1
print(ori)