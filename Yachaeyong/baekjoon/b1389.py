# 케빈 베이컨의 6단계 법칙
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            graph[s][e] = min(graph[s][e], graph[s][k]+graph[k][e])
ans = 0
bacon = INF
for r in range(1, N+1):
    temp = 0
    for c in range(1, N+1):
        temp += graph[r][c]
    if bacon > temp:
        bacon = temp
        ans = r
print(ans)
