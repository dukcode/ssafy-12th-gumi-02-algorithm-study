from collections import deque


def find(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    while q:
        cr, cc = q.popleft()
        if maze[cr][cc] == 3:
            return 1

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

    return 0


for _ in range(10):
    tc = int(input())
    N = 16
    maze = [list(map(int, input().strip())) for _ in range(N)]
    sr, sc = 1, 1
    print(f'#{tc} {find(sr, sc)}')
