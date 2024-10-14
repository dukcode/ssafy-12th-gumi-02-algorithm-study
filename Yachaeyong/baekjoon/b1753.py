import sys
from heapq import heappop, heappush

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (V + 1)
graph = [[] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue
            distance[next_node] = new_cost
            heappush(q, (new_cost, next_node))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
