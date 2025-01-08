# 듣보잡

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_heard = set()
for _ in range(n):
    no_heard.add(input().strip())

cnt = 0
result = []
for _ in range(m):
    no_see = input().strip()
    if no_see in no_heard:
        cnt += 1
        result.append(no_see)

result.sort()
print(cnt)
for idx in range(cnt):
    print(result[idx])




