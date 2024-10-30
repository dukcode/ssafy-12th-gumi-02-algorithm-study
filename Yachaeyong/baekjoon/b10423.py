# 전기가 부족해
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


N, M, K = map(int, input().split())
plants = list(map(int, input().split()))
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i
for i in range(K-1):
    union(parents[plants[i]], parents[plants[i+1]])
total = 0
for w, u, v in edges:
    if find(u) != find(v):
        # print(parents)
        # print(u, v)
        union(u, v)
        total += w

print(total)
# for edge in edges:
#     print(edge)