n=int(input())
fin=[]
for _ in range(n):
    s=tuple(input().split())
    fin.append(s)
fin.sort(key=lambda x: int(x[1])+int(x[2])+int(x[3]))

for i in fin:
    a, b, c,d = i
    print(a,b,c,d)