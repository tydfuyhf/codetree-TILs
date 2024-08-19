n = int(input())
fin = []

for _ in range(n):
    x = tuple(input().split())
    fin.append(x)

# 숫자값들을 내림차순으로 정렬하기 위해 int로 변환하고, 음수 부호를 사용하여 정렬
fin.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))

# 튜플을 리스트로 변환
for i in range(len(fin)):
    fin[i] = list(fin[i])
for i in fin:
    for w in i:
        print(w,end=" ")
    print()