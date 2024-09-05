x=list(map(int,input().split()))
y=list(map(int,input().split()))
total=[x,y]
widthsum=0
heightsum=0
for i in total:
    width=0
    for w in i:
        width+=w
    widthsum+=width
    print(round(width/4,1),end=" ")
print()
for c in range(4):
    height=0
    for v in range(2):
        height+=total[v][c]
    heightsum+=height
    print(round(height/2,1),end=" ")
print()
totalsum=(heightsum+widthsum)/16
print(round(totalsum,1))