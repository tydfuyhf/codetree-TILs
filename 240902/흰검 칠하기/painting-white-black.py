n = int(input())
commands = []

# 명령어를 입력받아 저장
for _ in range(n):
    x, d = input().split()
    x = int(x)
    commands.append((x, d))

size = 10000  # 충분히 큰 타일 배열
loc = size // 2  # 초기 위치를 중간으로 설정
color = [""] * size  # 타일 배열 초기화
cnt = [0] * size  # 각 타일이 몇 번 칠해졌는지 추적

for x, d in commands:
    if d == "R":
        for i in range(loc, loc + x):
            if cnt[i] == 0:  # 처음 칠할 때
                color[i] = "B"
            elif cnt[i] == 1 and color[i] == "W":  # 두 번째 칠할 때
                color[i] = "G"
            cnt[i] += 1
        loc += x  # 오른쪽으로 이동
    else:  # "L"
        for i in range(loc - x, loc):
            if cnt[i] == 0:  # 처음 칠할 때
                color[i] = "W"
            elif cnt[i] == 1 and color[i] == "B":  # 두 번째 칠할 때
                color[i] = "G"
            cnt[i] += 1
        loc -= x  # 왼쪽으로 이동

# 색깔별 타일 개수 계산
a = color.count("W")
b = color.count("B")
c = color.count("G")
print(a, b, c)