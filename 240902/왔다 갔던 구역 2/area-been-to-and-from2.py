n=int(input())
limit=0
collect=[]
for _ in range(n):
    x,d=input().split()
    x=int(x)
    limit+=x
    collect.append((x,d))
cnt=[0]*limit*2+[0]
loc=limit

for x,d in collect:
    if d=="R":
        for i in range(loc,loc+x):
            cnt[i]+=1
        loc+=x
    else:
        for i in range(loc-x,loc):
            cnt[i]+=1
        loc-=x
fin=0
for i in cnt:
    if i>=2:
        fin+=1
print(fin)