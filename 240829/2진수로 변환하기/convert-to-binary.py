n=int(input())
x=[]
if n==0 or n==1:
    print(n)    
else:    
    while True:
        x.append(n%2)
        if n//2==0 or n//2==1:
            x.append(n//2)
            break
        n=n//2
    x=x[::-1]
    for i in x:
        print(i,end="")