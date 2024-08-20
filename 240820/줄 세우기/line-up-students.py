n=int(input())
y=[]
cnt=1
#지금 문제는 튜플안에 cnt를 집어넣어야함 
for _ in range(n):
    x=tuple(input().split())
    x+=(cnt,)
    y.append(x)
    cnt+=1
y.sort(key=lambda x: (-int(x[0]),-int(x[1]),int(x[2])))
for idx,(h,w,num) in enumerate(y,start=1):
    print(h, w, num)