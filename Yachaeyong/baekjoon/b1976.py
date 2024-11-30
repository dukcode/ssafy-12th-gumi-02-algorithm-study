# 여행 가자

N = int(input())
M = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i


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
        parents[root_x] = root_x


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if cities[i][j]:
            union(i + 1, j + 1)

for i in range(1, N+1):
    parents[i] = find(i)

for i in range(1, M):
    if parents[plan[i]] != parents[plan[0]]:
        print('NO')
        break
else:
    print('YES')
