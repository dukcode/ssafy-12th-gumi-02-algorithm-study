# 네트워크 연결
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
M = int(input())

parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

total = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        total += c

print(total)