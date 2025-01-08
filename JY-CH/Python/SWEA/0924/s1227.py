# 미로1
from collections import deque


# 상 하 좌 우
DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

def exit(y, x, maze):
    queue = deque()
    visited[y][x] = 1
    queue.append((y,x))
    while queue:
        sy, sx = queue.popleft()
        if maze[sy][sx] == 3:
            return 1
        for direction in range(4):
            ny = sy + DY[direction]
            nx = sx + DX[direction]

            if 0 <= ny and ny < 100 and 0 <= nx and nx < 100 and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append((ny,nx))

    return 0










for num in range(1, 11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    for col in range(100):
        for row in range(100):
            if maze[col][row] == 2:
                y, x = col, row

    result = exit(y, x, maze)
    print(f'#{tc} {result}')
