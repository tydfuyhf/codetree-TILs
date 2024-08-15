n=int(input())
for _ in range(n):
    x=list(input().split())
    if x[2]=='Rain':
        for w in x:
            print(w,end=" ")
        break