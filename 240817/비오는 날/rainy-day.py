n=int(input())
fin=[]
ans=[]
for _ in range(n):
    x=list(input().split())
    if x[2]=='Rain':
        fin.append(x)
        y=list(x[0].split("-"))
        ans.append(y[0])

minindex=ans.index(min(ans))
for i in fin[minindex]:
    print(i,end=" ")