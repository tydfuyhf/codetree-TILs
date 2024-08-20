n=int(input())
y=[]
for _ in range(n):
    x=tuple(input().split())
    y.append(x)
y.sort(key=lambda x:(int(x[1]),-int(x[2])))
for i in y:
    a,b,c=i
    print(a,b,c)