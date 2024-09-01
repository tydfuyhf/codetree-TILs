n=int(input())
cnt=[]
for i in range(100):
    cnt.append(0)
for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x-1,y):
        cnt[i]+=1
print(max(cnt))