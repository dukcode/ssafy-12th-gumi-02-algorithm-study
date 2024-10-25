def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

n, m = map(int, input().split())
parent = [x for x in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1