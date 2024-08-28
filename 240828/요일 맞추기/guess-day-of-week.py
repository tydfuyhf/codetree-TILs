num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
m1,d1,m2,d2=map(int,input().split())
time1=d1
time2=d2
for i in range(1,m1):
    time1+=num_of_days[i]
for i in range(1,m2):
    time2+=num_of_days[i]

    
differ=(time2-time1)%7
print(day[differ])