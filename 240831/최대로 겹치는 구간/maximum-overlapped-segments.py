from collections import Counter
n=int(input())
x=[]
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b):
        x.append(i)
counter=Counter(x)
most_common = counter.most_common(1)[0]  # [(값, 빈도)] 형태로 반환됨
most_common_value = most_common[0]
most_common_count = most_common[1]
print(most_common_count)