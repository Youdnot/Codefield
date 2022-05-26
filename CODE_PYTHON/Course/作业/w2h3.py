a = int(input("请输入第一个整数"))
b = int(input("请输入第二个整数"))
import math
y = math.gcd(a,b)
n = int((a/y)*(b/y)*y)
print("{}、{}的最小公倍数是{}".format(a,b,n))
