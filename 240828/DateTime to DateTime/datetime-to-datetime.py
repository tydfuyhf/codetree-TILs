num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a,b,c=map(int,input().split())
time1=11*60*24+11*60+11
time2=a*60*24+b*60+c
if time1>=time2:
    print(-1)
else:
    print(time2-time1)