n,k=map(int,input().split())
y=[]
for i in range(n):
    y.append(0)
for _ in range(k):
    a,b=map(int,input().split())
    for i in range(a-1,b):
        y[i]+=1
print(max(y))