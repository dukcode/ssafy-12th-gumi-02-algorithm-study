def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i
for _ in range(M):
    w, a, b = map(int, input().split())

    if w == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')