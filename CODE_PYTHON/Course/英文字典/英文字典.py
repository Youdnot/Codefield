import json
def readinNouns():
    ln={}
    try:
        fo=open("d:/我的词典.txt",'r')
    except FileNotFoundError:
        fo=open("d:/我的词典.txt",'w+')
    for line in fo:
        ln=json.loads(line)
    fo.close()
    return ln
def printIntro(choice,ln):
    print('  我的英汉词典')
    print('-'*16)
    print('1.增加单词\n2.查询\n3.退出')
    choice=input('请选择（1-3）:') 
    if choice=='1':
        addNouns(choice,ln)
    elif choice=='2':
        searchNouns(choice,ln)
    elif choice=='3':
        savingNouns(ln)
    else:
        print('输入错误')
        print()
        printIntro(choice,ln)
    return ln
def addNouns(choice,ln): 
    noun=input('请输入英文单词：')
    tran=input('请输入中文释义：')
    if noun in ln.keys():
        if tran in ln[noun]:
            ln[noun]=ln[noun]
        else:
            ln[noun]=ln[noun]+';'+tran
    else:
        ln[noun]=tran
    print()
    printIntro(choice,ln) 
def savingNouns(ln):
    fo=open("d:/我的词典.txt",'w')
    lt=json.dumps(ln)
    fo.write(lt)
    fo.close()
def searchNouns(choice,ln):
    a=input('请输入英文单词：')
    if a in ln.keys():
        print('{}的中文意思是{}'.format(a,ln[a]))
    else:
        print('词典库里没有{}单词！'.format(a))
    print()
    printIntro(choice,ln)
def main():
    ln=readinNouns()
    choice=''
    printIntro(choice,ln)
    
choice=main()