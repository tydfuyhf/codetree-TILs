n,m=map(int,input().split())
x=[[0 for _ in range(m)] for _ in range(n)]
cnt=0
y=0
for i in range(m):
    for w in range(n):
        if y%2==0:
            x[w][i]=cnt

        else:
            x[n-w-1][i]=cnt
        cnt+=1
    y+=1
for i in x:
    for w in i:
        print(w,end=" ")
    print()