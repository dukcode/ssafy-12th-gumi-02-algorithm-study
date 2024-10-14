# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4

from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(start, target):
    q = [(0, start)]
    distance = [INF] * (v + 1)

    while q:
        dis, now = heappop(q)

        if distance[now] < dis:
            continue

        for next in adj_mat[now]:
            new_dis = dis + 1
            if new_dis < distance[next]:
                heappush(q, (new_dis, next))
                distance[next] = new_dis

    return distance[target]


v, e = map(int, input().split())
adj_mat = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    adj_mat[v1].append(v2)
    adj_mat[v2].append(v1)

x, k = map(int, input().split())
distance_to_k = dijkstra(1, k)
distance_to_x = dijkstra(k, x)

if distance_to_k + distance_to_x >= INF:
    print(-1)
else:
    print(distance_to_k + distance_to_x)
