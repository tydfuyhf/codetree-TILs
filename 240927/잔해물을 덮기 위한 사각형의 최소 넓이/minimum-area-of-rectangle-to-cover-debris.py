offset=1000
MaxR=2000
area=[[0]*(MaxR+1) for _ in range(MaxR+1)]
rect=[tuple(map(int,input().split())) for _ in range(2)]
cnt=0
length=[]
for x1,y1,x2,y2 in rect:
    x1,y1=x1+offset,y1+offset
    x2,y2=x2+offset,y2+offset
    for i in range(x1,x2):
        for w in range(y1,y2):
            if cnt==0:
                area[i][w]=1
            #여기 부분 아직 제대로 해결 못함
            else:
                area[i][w]=0
    cnt+=1
    length.append(x2-x1)
    length.append(y2-y1)
ans=0
for i in area:
    for w in i:
        ans+=w
for i in length[0:2]:
    if ans%i!=0:
        while ans%i!=0:
            ans+=1
print(ans)