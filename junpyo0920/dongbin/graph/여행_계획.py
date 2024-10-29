def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


n, m = map(int, input().split())
parents = [x for x in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(i, n):
        if arr[j]:
            union(i, j)

plan = list(map(lambda x: int(x) - 1, input().split()))
possible = True

for i in range(m - 1):
    if find(plan[i]) != find(plan[i + 1]):
        possible = False

print('YES' if possible else 'NO')
