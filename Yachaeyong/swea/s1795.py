from heapq import heappush, heappop


def dijkstra(start, graph):
    pq = []
    distance = [int(1e9)] * (N + 1)
    distance[start] = 0
    heappush(pq, (0, start))

    while pq:
        now_dist, now = heappop(pq)
        if distance[now] < now_dist:
            continue

        for next, cost in graph[now]:
            new_cost = now_dist + cost

            if new_cost >= distance[next]:
                continue

            distance[next] = new_cost
            heappush(pq, (new_cost, next))

    return distance


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    to_g = [[] for _ in range(N + 1)]
    from_g = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        to_g[x].append((y, c))
        from_g[y].append((x, c))

    to_ans = dijkstra(X, to_g)
    from_ans = dijkstra(X, from_g)

    max_dist = 0
    for i in range(1, N + 1):
        if max_dist < to_ans[i] + from_ans[i]:
            max_dist = to_ans[i] + from_ans[i]

    print(f'#{tc} {max_dist}')
