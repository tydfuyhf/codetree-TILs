num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a,b,c,d=map(int,input().split())
time1=b
time2=d+1
for i in range(1,a):
    time1+=num_of_days[i]
for i in range(1,c):
    time2+=num_of_days[i]
fin=time2-time1

print(fin)