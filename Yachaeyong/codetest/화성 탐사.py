from heapq import heappop, heappush

INF = int(1e9)


def dijkstra(sr, sc):
    q = []
    heappush(q, (mars[sr][sc], sr, sc))
    distance[sr][sc] = mars[sr][sc]

    while q:
        dist, cr, cc = heappop(q)

        if distance[cr][cc] < dist:
            continue

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                cost = dist + mars[nr][nc]
                # 현재 노드 거쳐서 다음 노드로 이동하는 비용이 더 적으면 이동
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heappush(q, (cost, nr, nc))


T = int(input())
for _ in range(T):
    N = int(input())
    mars = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    dijkstra(0, 0)
    print(distance[N-1][N-1])