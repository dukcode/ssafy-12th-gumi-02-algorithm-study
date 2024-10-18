# 파티

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph1[s].append((e, t))
    graph2[e].append((s, t))


def dijkstra(start, graph):
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
                heappush(q, (new_cost, next_node))
                distance[next_node] = new_cost
    return distance

# 갈 때
distance1 = dijkstra(X, graph1)
# 올 때
distance2 = dijkstra(X, graph2)

ans = 0
for i in range(1, N+1):
    ans = max(ans, distance1[i]+distance2[i])
print(ans)