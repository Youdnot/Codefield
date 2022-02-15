import random
randomnumber=[]
random.seed(10079)
for i in range(1000):
    randomnumber.append(random.randint(100,200))
ls={}
for i in randomnumber:
    ls[i]=ls.get(i,0)+1
result=sorted(ls.items(),key=lambda x:x[1], reverse=True)
lt=[result[0][0]]
for i in range(len(result)-1):
    if result[i+1][1]==result[0 ][1]:
        lt.append(result[i+1][0])
if len(lt)==len(result):
    print("没有众数")
else:
    print("众数是",end=" ")
    for i in lt:
        print(i,end=" ")