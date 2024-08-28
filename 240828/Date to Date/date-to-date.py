num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a,b,c,d=map(int,input().split())
time1=b
time2=d
for i in range(a-1):
    time1+=num_of_days[i]
for i in range(c-1):
    time2+=num_of_days[i]
print(time2-time1)