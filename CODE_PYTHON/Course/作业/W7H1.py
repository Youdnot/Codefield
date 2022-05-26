a=set(input("请输入字符串："))
result=0
for i in a:
    if ord(i) >= ord('0') and ord(i) <= ord('9'):
        result += int(i)
print("不同数字和为：%d" %(result))
