N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

ans = 0
for r in range(1, N + 1):
    cnt = 0
    for c in range(1, N + 1):
        # 해당 노드로 들어오거나 해당 노드에서 다른 노드로 나가면 cnt +1
        # 해당 노드에서 모든 노드에 대해 나가거나 들어오면 ans +1
        if graph[r][c] != INF or graph[c][r] != INF:
            cnt += 1
    if cnt == N:
        ans += 1

print(ans)