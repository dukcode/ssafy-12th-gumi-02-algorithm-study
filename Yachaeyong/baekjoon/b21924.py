# 도시 건설
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


def check():
    min_cost = 0
    for c, a, b in edges:
        if find(a) != find(b):
            # print(a, b, c)
            union(a, b)
            # print(parents)
            min_cost += c

    for i in range(1, N+1):
        parents[i] = find(parents[i])

    for i in range(1, N):
        if parents[i] != parents[i+1]:
            return -1
    return total_cost - min_cost


N, M = map(int, input().split())
edges = []
total_cost = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    total_cost += c

edges.sort()

parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i

print(check())

