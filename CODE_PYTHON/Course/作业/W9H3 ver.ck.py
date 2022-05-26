a=input("请输入一个字符串：")
lt=''.join(a.split()) 
ls={}
n=0
for i in lt:
    if i in ls:
        ls[i][0]=ls[i][0]+1
    else:
        ls[i]=[1,n]
    n=n+1
result=sorted(ls.items(),key=lambda x:(x[1][0],x[1][1]), reverse=True)
print("不重复的字符是:",end='')

for i in result: 
    print(i[0],end='')