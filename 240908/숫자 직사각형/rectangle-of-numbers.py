n,m=map(int,input().split())
arr=[i for i in range(1,n*m+1)]
fin=[]
cnt=0
x=[]
for i in arr:
    x.append(i)
    cnt+=1
    if cnt==m:
        fin.append(x)
        x=[]
        cnt=0

for i in fin:
    for w in i:
        print(w,end=" ")
    print()