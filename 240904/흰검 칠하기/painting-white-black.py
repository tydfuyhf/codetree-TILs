n=int(input())
maxsize=0
collect=[]
#왼쪽 흰색 오른쪽 검은색 / 각각 2번 이상 칠해지면 회색으로 
for _ in range(n):
    x,d=input().split()
    x=int(x)
    maxsize+=x
    collect.append((x,d))
loc=maxsize
cntW=[0 for _ in range(maxsize*2+1)]
cntB=[0 for _ in range(maxsize*2+1)]
color=["" for _ in range(maxsize*2+1)]
for x,d in collect:
    # black
    if d=="R":
        for i in range(loc,loc+x):
            if cntB[i]>=1 and cntW[i]>=2:
                color[i]="G"
                cntB[i]+=1
            else:
                color[i]="B"
                cntB[i]+=1
        loc=loc+x-1
    #white
    else:
        for i in range(loc-x+1,loc+1):
            if cntB[i]>=2 and cntW[i]>=1:
                color[i]="G"
                cntW[i]+=1
            else:
                color[i]="W"
                cntW[i]+=1
        loc=loc-x+1
    
a=color.count("W")
b=color.count("B")
c=color.count("G")
print(a,b,c)