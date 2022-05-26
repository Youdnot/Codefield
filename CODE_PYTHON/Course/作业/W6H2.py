import turtle
#定义进制转换
s=""
def convert(n,base):
    global s
    if n==0:
        s="0"
    else:
        while n>0:
            if n%base<=9:
                s=str(n%base)+s
            elif n%base == 10:
                s="A"+s
            elif n%base == 11:
                s="b"+s
            elif n%base == 12:
                s="C"+s
            elif n%base == 13:
                s="d"+s
            elif n%base == 14:
                s="E"+s
            elif n%base == 15:
                s="F"+s
            n=n//base      
    print(s)
#复用书本部分
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()    
    turtle.right(90)
def drawDigit(d): #根据字符绘制七段数码管
    drawLine(True) if d in ["2","3","4","5","6","8","9","A","b","d","E","F"] else drawLine(False)
    drawLine(True) if d in ["0","1","3","4","5","6","7","8","9","A","b","d"] else drawLine(False)
    drawLine(True) if d in ["0","2","3","5","6","8","9","b","C","d","E"] else drawLine(False)
    drawLine(True) if d in ["0","2","6","8","A","b","C","d","E","F"] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in ["0","4","5","6","8","9","A","b","C","d","E","F"] else drawLine(False)
    drawLine(True) if d in ["0","2","3","5","6","7","8","9","A","C","E","F"] else drawLine(False)
    drawLine(True) if d in ["0","1","2","3","4","7","8","9","A"] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
n=eval(input("请输入一个十进制整数:"))
base=eval(input("请输入进制:"))
convert(n,base)
turtle.setup(800,400)
turtle.pensize(5)
turtle.pencolor("red")
for i in s:
    drawDigit(i)

