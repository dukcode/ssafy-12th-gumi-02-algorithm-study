from collections import deque

# 미로의 거리

# 출발지 탐색 함수

# 0을 찾아 떠나는 함수
## 이때 이 함수는 지나간 곳을 다시 들려선 안됨, 방문 표시 필요
# 3이면 멈추고 뱉어낼것.

# 상 하 좌 우
DY = (-1 , 1, 0 ,0)
DX = (0, 0, -1, 1)





def maze_out(y, x, maze):
    queue = deque()
    visited[y][x] = 1
    queue.append((y, x))
    while queue:
        sy, sx = queue.popleft()
        if maze[sy][sx] == 3:
            return visited[sy][sx] - 2
        for direct in range(4):
            ny = sy + DY[direct]
            nx = sx + DX[direct]

            if 0 <= ny and ny < n and 0 <= nx and nx < n and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[sy][sx] + 1
                queue.append((ny,nx))

    return 0


for tc in range(int(input())):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for col in range(n):
        for row in range(n):
            if maze[col][row] == 2:
                y, x = col, row
    result = maze_out(y, x, maze)
    print(f'#{tc+1} {result}')
