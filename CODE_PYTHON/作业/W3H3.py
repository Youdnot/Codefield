a = eval(input("输入开始数字:"))
b = eval(input("输入结束数字:"))
j = 1
for i in range(a,b+1):
    if i == b:
      print(i)
    elif j != 5:
      print (i,end=',')
      j = j + 1      
    else:
      print(i)
      j = 1        
