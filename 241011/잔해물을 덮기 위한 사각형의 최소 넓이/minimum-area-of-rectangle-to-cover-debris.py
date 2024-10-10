rectangle_coordinate=[tuple(map(int,input().split()))]
out_coordinate=[tuple(map(int,input().split()))]
Max_index=1000
coordinate=[[0]*(Max_index*2+1) for _ in range(Max_index*2+1)]
row=0
col=0
for x1,y1,x2,y2 in rectangle_coordinate:
    x1,y1=x1+Max_index,y1+Max_index
    x2,y2=x2+Max_index,y2+Max_index
    for i in range(x1,x2):
        for w in range(y1,y2):
            coordinate[i][w]=1
    row=x2-x1
    col=y2-y1
cnt=0
for x1,y1,x2,y2 in out_coordinate:
    x1,y1=x1+Max_index,y1+Max_index
    x2,y2=x2+Max_index,y2+Max_index
    for i in range(x1,x2):
        for w in range(y1,y2):
            coordinate[i][w]=0
for i in rectangle_coordinate:
    for w in i:
        cnt+=1
if cnt%row!=0 or cnt%col!=0:
    cnt=row*col
print(cnt)