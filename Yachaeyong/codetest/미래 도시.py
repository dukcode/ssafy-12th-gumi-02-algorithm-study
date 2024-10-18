N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for r in range(1, N + 1):
    graph[r][r] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

ans = graph[1][K] + graph[K][X]

if ans >= INF:
    print(-1)
else:
    print(ans)
