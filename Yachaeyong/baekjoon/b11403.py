# 경로 찾기
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for s in range(N):
        for e in range(N):
            # 가중치 없고 s->e가는 간선이 존재하는지만 알면 되므로 min 비교 안 함
            if graph[s][k] and graph[k][e]:
                graph[s][e] = 1

for r in range(N):
    for c in range(N):
        print(graph[r][c], end=' ')
    print()
