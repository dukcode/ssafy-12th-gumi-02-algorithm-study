from heapq import heappop, heappush


def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q, (0, start))

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


N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))
    graph[B].append((A, 1))

dijkstra(1)

hide_idx = 0
max_distance = 0
cnt = 0
for i in range(1, N + 1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        hide_idx = i
        cnt = 1
    elif max_distance == distance[i]:
        cnt += 1
print(hide_idx, max_distance, cnt)
'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
