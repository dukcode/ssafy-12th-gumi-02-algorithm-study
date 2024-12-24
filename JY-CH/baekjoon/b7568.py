# 덩치

import sys
input = sys.stdin.readline



n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))


# 또 람다쓰면 어지러웠을지도
# 등수용 배열
grade = [1] * n


for i in range(n):
    for j in range(n):
        if i != j:
            # 두 조건 다 밀려야 순위가 강등됨
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                grade[i] += 1

print(*grade)