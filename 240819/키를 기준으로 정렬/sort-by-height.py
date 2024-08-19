n=int(input())
fin=[]
for _ in range(n):
    x=list(input().split())
    fin.append(x)
fin.sort(key=lambda x : x[1])
for i in fin:
    for w in i:
        print(w,end=" ")
    print()