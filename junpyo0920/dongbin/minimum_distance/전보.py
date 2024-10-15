from heapq import heappush, heappop

INF = int(1e9)


def dijkstra(start):
    q = [(0, start)]
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        cur_dis, cur_node = heappop(q)

        if distance[cur_node] < cur_dis:
            continue

        for next_dis, next_node in adj_list[cur_node]:
            new_dis = cur_dis + next_dis
            if new_dis < distance[next_node]:
                distance[next_node] = new_dis
                heappush(q, (new_dis, next_node))

    cnt = 0
    max_dis = 0
    for dis in distance:
        if dis != INF and dis != 0:
            cnt += 1
            max_dis = max(max_dis, dis)

    print(cnt, max_dis)


n, m, c = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, w = map(int, input().split())
    adj_list[x].append([w, y])

dijkstra(c)
