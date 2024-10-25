import sys

N = int(input())
tunnels = []
planet_x = []
planet_y = []
planet_z = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())

    planet_x.append((x, i))
    planet_y.append((y, i))
    planet_z.append((z, i))

planet_x.sort()
planet_y.sort()
planet_z.sort()

for now_planet in planet_x, planet_y, planet_z:
    for i in range(1, N):
        w1, s = now_planet[i - 1]
        w2, e = now_planet[i]
        cost = abs(w1 - w2)
        tunnels.append((cost, s, e))

tunnels.sort()

parent = [0] * N
for i in range(N):
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


total_cost = 0
for cost, s, e in tunnels:
    if find(s) != find(e):
        union(s, e)
        total_cost += cost

print(total_cost)
