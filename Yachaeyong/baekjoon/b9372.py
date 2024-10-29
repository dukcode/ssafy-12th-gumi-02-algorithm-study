# 상근이의 여행

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


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))

    parents = [0] * (N + 1)
    for i in range(1, N + 1):
        parents[i] = i

    planes = 0
    for a, b in edges:
        if find(a) != find(b):
            union(a, b)
            planes += 1

    print(planes)
