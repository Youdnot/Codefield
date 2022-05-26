sum=0
for i in range(2,101):
    n=0
    for j in range(2,i):
        print(i%j)
        if i%j==0:
            n=1
            break
    if n==1:
        n=0
        continue
    elif n==0:
        sum+=i
print(sum)

