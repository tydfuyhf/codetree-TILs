a,b=map(int,input().split())
x=list(input())
x=x[::-1]
x=map(int,x)
num=0
cnt=0
for i in x:
    num=num+i*a**cnt
    cnt+=1
y=[]
while num>=b:
    y.append(num%b)
    num=num//b
y.append(num)
y=y[::-1]
for i in y:
    print(i,end="")