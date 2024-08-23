n = int(input())  # 수열의 길이 N을 입력 받음
first = list(map(int, input().split()))  # 수열을 입력 받음
second = sorted(first)  # 수열을 오름차순으로 정렬

# 각 원소가 정렬된 수열에서 어디로 이동했는지 저장할 리스트
index_mapping = []

# 각 원소에 대해 그 원소가 정렬된 리스트에서의 인덱스를 찾음
for num in first:
    index = second.index(num)
    index_mapping.append(index)
    # 이미 사용한 인덱스를 재사용하지 않기 위해 -1로 바꿈
    second[index] = -1
index_mapping=[i+1 for i in index_mapping]
for w in index_mapping:
    print(w,end=" ")