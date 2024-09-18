from heapq import heappush, heappop
from math import sqrt


def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return find_set(p[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        p[root_y] = root_x
    else:
        p[root_x] = root_y


n, m = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]
hq = []
p = [x for x in range(n + 1)]

for i in range(1, n):
    for j in range(i + 1, n + 1):
        v1, v2 = data[i - 1], data[j - 1]
        cost = sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
        heappush(hq, (cost, i, j))

for _ in range(m):
    v1, v2 = map(int, input().split())
    union(v1, v2)

parents = set()
for i in range(1, n + 1):
    parents.add(find_set(p[i]))

cnt = len(parents)
ans = 0
while cnt > 1 and hq:
    w, v1, v2 = heappop(hq)
    if find_set(v1) != find_set(v2):
        union(v1, v2)
        ans += w
        cnt -= 1

print(f"{ans:.2f}")
