from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    while q:
        cr, cc = q.popleft()
        if cr == N and cc == M:
            return
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + 1

bfs(0,0)
print(visited[N-1][M-1])
