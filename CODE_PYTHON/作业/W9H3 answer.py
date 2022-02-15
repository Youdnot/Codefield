s=input("请输入一个字符串:")
s=s.replace(" ","")  #删除空格
b=set(s)  #保留唯一的字符
d={}
for a in b:  #要把出现位置也保存起来
    d[a] = (s.count(a),s.index(a))
#按出现次数降序排序，按原来位置升序    
a=sorted(d.items(),key=lambda x:(-x[1][0],-x[1][1]))
#输出原来的字符
print("不重复的字符是:",end='')
for i in a:
    print(i[0],end='') 