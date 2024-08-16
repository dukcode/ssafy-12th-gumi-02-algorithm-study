def bfs(sr, sc, h):
    Q = []
    Q.append([sr, sc])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    while Q:
        cr, cc = Q.pop(0)
        if area[cr][cc] > h:
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and area[nr][nc]:
                Q.append([nr, nc])
                visited[nr][nc] = 1
    return visited


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
max_h = 0
# 최대 높이
for i in range(N):
    for j in range(N):
        if max_h < area[i][j]:
            max_h = area[i][j]

for h in range(6, 7):
    if
    print(bfs(0, 0))
    print('-----------------')
# h = 6
# for row in bfs(0, 0):
#     print(row)