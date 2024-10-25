N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))

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


for i in range(N):
    for j in range(N):
        if data[i][j]:
            union(i + 1, j + 1)

is_available = True
for i in range(len(plans) - 1):
    if find(plans[i]) != find(plans[i + 1]):
        is_available = False
        break

if is_available:
    print('YES')
else:
    print('NO')

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
