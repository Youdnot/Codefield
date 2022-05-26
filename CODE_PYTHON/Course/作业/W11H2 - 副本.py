import json
fr=open("2015年5月高三模拟考成绩.csv","r")
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(','))
fr.close()
fw=open("2015年5月高三模拟考成绩.json","w")
for i in range(q,len(ls)):
    ls[i]=dict(zip(ls[0],ls[1]))
json.dump(ls[1:],fw,sort_keys=True,indent=4)
fw.close

