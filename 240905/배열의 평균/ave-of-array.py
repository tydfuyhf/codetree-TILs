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
    print(width/4,end=" ")
print()
for c in range(4):
    height=0
    for v in range(2):
        height+=total[v][c]
    heightsum+=height
    print(height/2,end=" ")
print()
totalsum=(heightsum+widthsum)/16
print(totalsum)