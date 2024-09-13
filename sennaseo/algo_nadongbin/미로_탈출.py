from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] += arr[x][y]
    return arr[n-1][m-1]


print(f'{bfs(0, 0)}')
