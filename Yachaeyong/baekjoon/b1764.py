# 듣보잡

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

h = set(input().strip() for _ in range(N))
m = set(input().strip() for _ in range(M))

ans = [*(h & m)]
ans.sort()
print(len(ans))
for a in ans:
    print(a)
