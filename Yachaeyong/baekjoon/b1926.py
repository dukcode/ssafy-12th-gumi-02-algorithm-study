# 1926 그림 S1

n, m = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(sr, sc):
    Q = []
    Q.append([sr, sc])
    visited[sr][sc] = 1
    a = 1

    while Q:
        cr, cc = Q.pop(0)

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and canvas[nr][nc]:
                Q.append([nr, nc])
                visited[nr][nc] = 1
                a += 1
    # 그림 넓이
    return a


area = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = max(bfs(i, j), area)

print(cnt)
print(area)
