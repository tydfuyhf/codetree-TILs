n=list(input())
n=n[::-1]
n=map(int,n)
cnt=0
num=0
for i in n:
    num=i*2**cnt+num
    cnt+=1
num*=17
x=[]
while num>=2:
    x.append(num%2)
    num=num//2
x.append(num)
x=x[::-1]
for i in x:
    print(i,end="")