file=open("成绩.csv","r")
ls=[]
for line in file:
    line=line.replace("\n","")
    ls.append(line.split(','))
file.close()
lt={}
for i in ls:
    info=[]
    info.append(i[0])
    info.append(eval(i[1])+eval(i[2])+eval(i[3]))
    lt[info[0]]=info[1]
print(lt)
final=sorted(lt.items(), key=lambda x:x[1], reverse=True)
print('学号\t总分\t')
for i in final:
    print(i[0]+'\t'+str(i[1]))