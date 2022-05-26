import os #判断txt文件是否为空使用，防止产生第一行换行空行导致无法读入

def readfile(): #读取文件
    try:
        file=open("我的词典.txt",'r')
    except FileNotFoundError:
        file=open("我的词典.txt",'w+')
    #尝试是否存在txt文件，存在则读取，不存在则创建
    di={}
    for line in file:
        a=line.split(",")
        di[a[0]]=a[1]
    file.close
    return di

def printInfo(): #输出介绍信息
    print("{:^8}".format("我的英汉词典"))
    print('-'*14)
    print("1.增加单词\n2.查询\n3.退出")

def getIntro():
    option=input("请选择（1-3）：")
    return option

def choose(option,di):
    if option=='1':
        add(di)
    elif option=='2':
        search(di)
    elif option=='3':
        ex()
    else:
        print("输入错误")

def add(di):
    ad1=input("请输入英文单词：")
    ad2=input("请输入中文释义：")
    #可以修改字典，然后覆盖写入txt，但效率低(di[ad1]=ad2)
    #多重释义（只能做到添加一项新的词条，旧词条未删除，数据冗余；读取的数据为最后一项，对查询结果无影响）
    if ad1 in di:
        ad2=di[ad1]+';'+ad2
    file=open("我的词典.txt",'a')
    size = os.path.getsize('我的词典.txt')
    if size == 0:
        file.write("{},{}".format(ad1,ad2))
    else:
        file.write("\n{},{}".format(ad1,ad2))
    file.close()

def search(di):
    word=input("请输入英文单词：")
    if word in di:
        print("{}的中文意思是{}".format(word,di[word]))
    else:
        print("词典里没有{}单词".format(word))

def ex():
    print("词典退出")

def main():
    di=readfile() #读取文件
    printInfo() #输出介绍信息
    option=getIntro() #获取输入选项
    choose(option,di) #选择执行程序
    return option

option=main()
print('\n')  
while option!='3':    
    option=main()
    print('\n')