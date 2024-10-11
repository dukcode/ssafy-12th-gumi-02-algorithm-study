from heapq import heappop, heappush

INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


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


dijkstra(C)

cnt = 0
max_distance = 0

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)