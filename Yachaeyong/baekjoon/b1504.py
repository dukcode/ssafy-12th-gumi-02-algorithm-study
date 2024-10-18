# 특정한 최단 경로
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    q = []
    heappush(q, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heappush(q, (new_cost, next_node))
    return distance[end]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

ans = min(path1, path2)
if ans >= INF:
    print(-1)
else:
    print(ans)
# print(ans if ans < INF else -1)
