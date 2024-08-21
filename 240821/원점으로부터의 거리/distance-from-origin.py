n=int(input())
q=[]
cnt=0
for _ in range(n):
    x,y=map(int,input().split())
    cnt+=1
    q.append((x,y,cnt))
q.sort(key=lambda x: abs(x[0])+abs(x[1]))
for i in q:
    a,b,c=i
    print(c)