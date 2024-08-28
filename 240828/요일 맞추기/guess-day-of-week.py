num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
m1,d1,m2,d2=map(int,input().split())
time1=d1
time2=d2
for i in range(1,m1):
    time1+=i
for i in range(1,m2):
    time2+=i
if time2-time1>0:
    differ=1-(time2-time1)%7
else:
    differ=1-abs(time2-time1)%7
print(day[differ])