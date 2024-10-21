# 좌표 정렬하기 2

import sys

input = sys.stdin.readline

N = int(input())
coordinate = [list(map(int, input().split())) for _ in range(N)]
coordinate.sort(key=lambda x: (x[1], x[0]))

for c in coordinate:
    print(*c)
