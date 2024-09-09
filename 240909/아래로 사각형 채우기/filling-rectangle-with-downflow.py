n=int(input())
x=[[0 for _ in range(n)] for _ in range(n)]
cnt=0
for i in range(n):
    for w in range(n):
        cnt+=1
        x[w][i]=cnt
for i in x:
    for w in i:
        print(w,end=" ")
    print()