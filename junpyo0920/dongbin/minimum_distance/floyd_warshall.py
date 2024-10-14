# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

n = int(input())
e = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    graph[x][x] = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a][b] = w

for k in range(1, n + 1):
    for a in range(1, n + 1):
        if k == a:
            continue
        for b in range(1, n + 1):
            if a == b:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b] if graph[a][b] != INF else 'INF', end=" ")
    print()