n=int(input())
offset=100
MaxR=200
check=[[0]*(MaxR+1) for _ in range(MaxR+1)]
area=[tuple(map(int,input().split())) for _ in range(n)]

for x,y in area:
    for i in range(x,x+8):
        for w in range(y,y+8):
             check[i][w]=1
cnt=0
for i in check:
    for w in i:
        cnt+=w
print(cnt)