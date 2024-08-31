n,b=map(int,input().split())
x=[]
while n>=b:
    x.append(n%b)
    n=n//b
x.append(n)
x=x[::-1]
for i in x:
    print(i,end="")