# 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())

time_table = []
for _ in range(n):
    start, end = map(int, input().split())
    time_table.append((start, end))

# 정렬
time_table.sort(key=lambda x: (x[1], x[0]))

# 그리디
# 지입으로 그리디라면서 최적해 접근하듯이 생각함
# 에휴
cnt = 0
time = 0
for start, end in time_table:
    if start > time:
        cnt += 1
        time = end

print(cnt)


