n=int(input())
limit=0
collect=[]
#왼쪽 흰색 오른쪽 검은색 / 2번 이상 칠해지면 회색으로 
for _ in range(n):
    x,d=input().split()
    x=int(x)
    limit+=x
    collect.append((x,d))
loc=limit
cnt=[0 for _ in range(limit*2+1)]
color=["" for _ in range(limit*2+1)]
for x,d in collect:
    # black
    if d=="R":
        for i in range(loc,loc+x):
            if cnt[i]<2:
                color[i]="B"
                cnt[i]+=1
            else:
                color[i]="G"
        loc+=x
    #white
    else:
        for i in range(loc-x,loc):
            if cnt[i]<2:
                color[i]="W"
            else:
                color[i]="G"
                cnt[i]+=1
        loc-=x
a=color.count("W")
b=color.count("B")
c=color.count("G")
print(a,b,c)