# 최소비용 구하기
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, u = map(int, input().split())
    graph[a].append((b, u))
s, e = map(int, input().split())


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

            if new_cost < distance[next_node]:
                heappush(q, (new_cost, next_node))
                distance[next_node] = new_cost


dijkstra(s)

print(distance[e])
