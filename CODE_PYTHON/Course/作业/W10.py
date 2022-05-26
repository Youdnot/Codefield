#(1)
import random
random.seed(1000)
a=open("data.txt","wt")
def f_write():
    for i in range(10):
        num=random.randint(3,8)
        for i in range(num):
            a.write(str(random.randint(-50,50))) 
            if i == num-1:
                a.write('\n')
            else:
                a.write(',')
f_write()
a.close
#for text
a=open("data.txt","r")
for line in a:
    print(line)
a.close

#(2)
def f_read():
    a=open("data.txt","rt")
    num=a.read()
    x=num.replace('\n',',',9)
    y=x.replace('\n','',-1)
    lt=y.split(',')
    ori=0
    print(lt)
    for i in lt:
        if eval(i)>ori:
            ori=eval(i)
        else:
            continue
    print('用read求全部数字的最大值:{}'.format(ori))
f_read()
a.close


#3
def r_readlines():
    a=open("data.txt","rt")
    num=a.readlines()
    num1=[]
    for i in num:
        x=i.replace('\n','')
        num1.append(x)
    print(num1)
    ls=[]
    for i in num1:
        lt=i.split(',')
        print(lt)
        su=0
        for j in lt:
            su+=int(j)
        ls.append(su)
    print(ls)
    print('用readlines求每行和的最大值：{}'.format(max(ls)))
r_readlines()
a.close