# 행성 연결
import sys

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


N = int(input())
planets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i

edges = []
for i in range(N):
    for j in range(i + 1, N):
        if planets[i][j]:
            edges.append((planets[i][j], i + 1, j + 1))

edges.sort()

total = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost

print(total)
