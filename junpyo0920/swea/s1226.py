N = 16
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find_start_pos(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x


def find_root(sy, sx):
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1
    queue = [(sy, sx)]
    while queue:
        cur_y, cur_x = queue.pop(0)
        if maze[cur_y][cur_x] == 3:
            return 1
        for d in range(4):
            ny, nx = cur_y + dy[d], cur_x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] != 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = 1
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sy, sx = find_start_pos(maze)
    ans = find_root(sy, sx)
    print(f'#{tc} {ans}')