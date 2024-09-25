n=int(input())
rect=[tuple(map(int,input().split())) for _ in range(n)]
MaxR=200
OFFSET=100
checked = [
    [0] * (MaxR + 1)
    for _ in range(MaxR + 1)
]
for x1,y1,x2,y2 in rect:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = 1
area = 0
for x in range(0, MaxR + 1):
    for y in range(0, MaxR + 1):
        if checked[x][y]:
            area += 1
print(area)