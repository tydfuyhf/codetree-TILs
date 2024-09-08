x=[]
y=[]
fin=[[0 for _ in range(3)] for _ in range(3)]
for _ in range(3):
    w=list(map(int,input().split()))
    x.append(w)
p=list(input())
for _ in range(3):
    c=list(map(int,input().split()))
    y.append(c)
for i in range(3):
    for e in range(3):
        fin[i][e]=x[i][e]*y[i][e]
        print(fin[i][e],end=" ")
    print()