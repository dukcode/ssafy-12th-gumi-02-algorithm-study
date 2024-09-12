from heapq import heappush, heappop


def dijkstra(sr, sc):
    q = []
    heappush(q, (0, sr, sc))
    cost[sr][sc] = 0

    while q:
        now_cost, cr, cc = heappop(q)
        if cost[cr][cc] < now_cost:
            continue

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = now_cost + data[nr][nc]
                if new_cost >= cost[nr][nc]:
                    continue

                cost[nr][nc] = new_cost
                heappush(q, (new_cost, nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().strip())) for _ in range(N)]
    INF = 1e9
    cost = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{tc} {cost[N - 1][N - 1]}')
