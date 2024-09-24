import sys
from heapq import heappop, heappush

INF = 0xFFFFFFFF
input = sys.stdin.readline


def dijkstra(start):
    hq = [(0, start)]
    distance = [INF] * (V + 1)
    distance[start] = 0

    while hq:
        cur_dis, cur_node = heappop(hq)
        if cur_dis <= distance[cur_node]:
            for next_node, next_dis in adj_list[cur_node]:
                new_dis = cur_dis + next_dis
                if new_dis < distance[next_node]:
                    distance[next_node] = new_dis
                    heappush(hq, (new_dis, next_node))

    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])


V, E = map(int, input().split())
K = int(input())
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

dijkstra(K)