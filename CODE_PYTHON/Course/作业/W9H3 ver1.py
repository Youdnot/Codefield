a=input("请输入一个字符串：")
lt=''.join(a.split()) #字符串重组
ls={}
for i in lt:
    ls[i]=ls.get(i,0)+1
result=sorted(ls.items(),key=lambda x:x[1], reverse=True)
print(result)
print("不重复的字符是:",end='')
for i in result:
    print(i[0],end='')