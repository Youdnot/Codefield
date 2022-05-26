file=open("2015年5月高三模拟考成绩.csv","r",encoding="utf-8")
ls=[]
for line in file:
    if line[0]=="3":
        line=line.replace("\n","")
        ls.append(line.split(","))
file.close
lt=['名次','班别','姓名','总分']
end=[]
for i in range(len(ls)):
    a={}
    a[lt[1]]=ls[i][1]
    a[lt[2]]=ls[i][2]
    s=0
    for j in range(3,9):
        s+=eval(ls[i][j])
    a[lt[3]]=s
    end.append(a)
end1=end[:]
result=sorted(end1,key=lambda x:-x['总分'])
print("总分前5名的学生情况")
print("名次\t班别\t姓名\t总分",chr(12288))
print('----------------------------')
for i in range(5):
    l="{:^3}\t{:^}\t{:^}\t{:<5}".format(i+1,result[i]['班别'],result[i]['姓名'],result[i]['总分'],chr(12288))
    print(l,chr(12288))


