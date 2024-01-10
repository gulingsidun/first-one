#限制次数控制
n=0
shuru=input("输入数字")
while shuru!="":
    n=eval(shuru)+n
    shuru=input()
print(n)
