N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

edges.sort(key=lambda x: x[2])

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


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


cost = 0
max_cost = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c
        max_cost = c

print(cost - max_cost)
