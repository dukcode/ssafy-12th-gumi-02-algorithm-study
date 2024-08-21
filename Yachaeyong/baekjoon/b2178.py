# 2178 미로 탐색 S1

N, M = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(N)]

sr, sc = 0, 0
Q = []
Q.append([sr, sc])
visited = [[0] * M for _ in range(N)]
visited[sr][sc] = 1
cnt = 0

while Q:
    cr, cc = Q.pop(0)
    if cr == N-1 and cc == M-1:
        cnt = visited[cr][cc]
        break

    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = cr + dr
        nc = cc + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and miro[nr][nc]:
            Q.append([nr, nc])
            visited[nr][nc] = visited[cr][cc] + 1

print(cnt)
