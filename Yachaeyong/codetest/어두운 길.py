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
roads = []
origin_cost = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    roads.append((x, y, z))
    origin_cost += z

roads.sort(key=lambda a: a[2])

parent = [0] * N
for i in range(N):
    parent[i] = i

min_cost = 0
for x, y, z in roads:
    if find(x) != find(y):
        union(x, y)
        min_cost += z

print(origin_cost - min_cost)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
