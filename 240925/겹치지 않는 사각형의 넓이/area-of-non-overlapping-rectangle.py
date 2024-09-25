MaxR=2000
offset=1000
x=[tuple(map(int,input().split())) for _ in range(3)]
check=[[0]*(MaxR+1) for _ in range(MaxR+1)]
cnt=0
for x1,y1,x2,y2 in x:
    x1,y1=x1+offset,y1+offset
    x2,y2=x2+offset,y2+offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            if cnt!=2:
                check[i][j]=1
            elif cnt==2:
                check[i][j]=0
    cnt+=1
area=0
for i in check:
    for w in i:
        area+=w
print(area)