# 회의실 배정
import sys

N = int(sys.stdin.readline())
table = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    table.append([a, b])

# key로 정렬
# 2차원 배열은 () 튜플로 묶어서 정렬함
# x[1], x[0] == 인덱스 1번 기준으로 오름차순 정렬하고 같은 값이면 0번 기준으로 오름차순 정렬
table.sort(key=lambda x: (x[1], x[0]))

pre_end = 0
cnt = 0

for new_start, new_end in table:
    if pre_end <= new_start:
        cnt += 1
        pre_end = new_end

print(cnt)
