# 전력난
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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    roads = []
    max_total = 0
    for _ in range(n):
        data = list(map(int, input().split()))
        if len(data) == 3:
            x, y, z = data[0], data[1], data[2]
            roads.append((z, x, y))
            max_total += z

    roads.sort()

    parents = [0] * (m + 1)
    for i in range(1, m + 1):
        parents[i] = i

    min_total = 0
    for z, x, y in roads:
        if find(x) != find(y):
            union(x, y)
            min_total += z

    print(max_total - min_total)
