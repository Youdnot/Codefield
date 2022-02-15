a = eval(input("请输入系数a:"))
b = eval(input("请输入系数b:"))
c = eval(input("请输入系数c:"))
d = b**2-4*a*c

if a == 0:
   print("不是一元二次方程")
elif d == 0:
     print("方程有两个相等的实根 x1=x2={:.1f}".format(-a))
elif d < 0:
     print("方程有两个共轭虚根")
     e1 = -b/(2*a)
     e2 = (-d)**0.5/(2*a)
     e3 = -e2
     print("x1= {}".format(complex(e1,e2)))
     print("x2= {}".format(complex(e1,e3)))
else:
     print("方程有两个不等实根")
     print("x1= {},x2= {}".format((-b+(d**0.5))/(2*a),(-b-(d**0.5))/(2*a)))
