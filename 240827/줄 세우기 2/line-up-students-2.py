n=int(input())
x=[]
cnt=0
for _ in range(n):
    cnt+=1
    y=tuple(map(int,input().split()))
    y=y+(cnt,)
    x.append(y)
x.sort(key=lambda x: (x[0],-x[1]))
for i in x:
    a,b,c=i
    print(a,b,c)