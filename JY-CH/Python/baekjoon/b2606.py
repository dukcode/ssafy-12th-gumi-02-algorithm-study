# 바이러스

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

m = int(input())


def infection():
    queue = deque([1])  
    visited = [False] * (n + 1)
    visited[1] = True
    cnt = 0

    while queue:
        current_pos = queue.popleft()
        for com in data[current_pos]:
            if not visited[com]:
                visited[com] = True
                queue.append(com)
                cnt += 1

    return cnt



data = [[] for _ in range (n + 1)]

for _ in range(1, m + 1):
    start, end = map(int, input().split())
    data[start].append(end)
    data[end].append(start)

print(infection())