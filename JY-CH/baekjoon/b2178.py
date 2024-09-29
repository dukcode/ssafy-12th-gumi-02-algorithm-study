# 미로 탐색
from collections import deque

DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

def bfs(n, m, maze):
    queue = deque()
    visited[0][0] = 1
    queue.append((0, 0))
    while queue:
        sy, sx = queue.popleft()
        if sy == n - 1 and sx == m - 1:
            return visited[sy][sx]

        for direction in range(4):
            ny = sy + DY[direction]
            nx = sx + DX[direction]

            if 0 <= ny and ny < n and 0 <= nx and nx < m and maze[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[sy][sx] + 1
                queue.append((ny,nx))

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = bfs(n, m, maze)
print(result)