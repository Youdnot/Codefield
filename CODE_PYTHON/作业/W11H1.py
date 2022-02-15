a=open("阶乘.txt","w")
base=1
for i in range(1,101):
    base=i*base
    a.write("{}！={}".format(i,base))
    a.write('\n')
a.close
