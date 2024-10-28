def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


n, m = map(int, input().split())
parents = [x for x in range(n + 1)]

arr = []

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))

totalDistance = 0
longestDistance = 0

arr.sort()

for (c, a, b) in arr:
    if find(a) != find(b):
        union(a, b)
        totalDistance += c
        longestDistance = c

print(totalDistance - longestDistance)