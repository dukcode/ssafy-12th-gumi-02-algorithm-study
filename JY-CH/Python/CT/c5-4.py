# 미로 탈출
from collections import deque

# 상하좌우
# 앞으론 리스트 대신 튜플을
# 절대적인건 대문자로
DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)



def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        sy, sx = queue.popleft()
        for way in range(4):
            ny = sy + DY[way]
            nx = sx + DX[way]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if maze[ny][nx] == 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[sy][sx] + 1
                queue.append((ny,nx))

    return maze[n-1][m-1]









n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
result = bfs(0,0)
print(result)