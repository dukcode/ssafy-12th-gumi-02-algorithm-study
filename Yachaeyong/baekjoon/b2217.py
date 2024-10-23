# 로프

import sys

N = int(input())

ropes = [int(sys.stdin.readline()) for _ in range(N)]
ropes.sort(reverse=True)

max_weight = 0

for k in range(N):
    max_weight = max(max_weight, ropes[k] * (k + 1))

print(max_weight)
