y=[]
for _ in range(5):
    x=tuple(input().split())
    y.append(x)
y.sort(key= lambda x: x[0])
print("name")
for i in y:
    a,b,c=i
    print(a,b,c)
y.sort(key=lambda x: -int(x[1]))
print()
print("height")
for i in y:
    a,b,c=i
    print(a,b,c)